import os

import ipyleaflet as L
import xarray as xr
from shiny import App, render, ui
from shinywidgets import output_widget, render_widget

server = os.environ.get("SERVER", "https://thredds.niva.no")
dataset_name = os.environ.get("DATASET", "msource-outlet.nc")
ds = xr.open_dataset(f"{server}/thredds/dodsC/datasets/{dataset_name}")

app_ui = ui.page_fluid(
    ui.h2("Shiny python docker"),
    ui.markdown(
        f"""Plotting **{ds.attrs["title"]}**

    {ds.attrs["summary"]}

    from ENV: 
        - SERVER={server}
        - DATASET={dataset_name}
    """
    ),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_select(
                "data_var",
                "Data variables",
                [v for v in ds.data_vars if v != "station_name"],
            ),
            output_widget("map"),
        ),
        ui.panel_main(ui.output_plot("plot")),
    ),
    ui.output_table("data_table")
)


def server(input, output, session):
    @output
    @render.plot
    def plot():
        return ds[input.data_var()].sel(time="2023").plot()

    @output
    @render_widget
    def map():
        location = [float(ds.latitude.values), float(ds.longitude.values)]
        m = L.Map(basemap=L.basemaps.OpenStreetMap.Mapnik, center=location)
        m.add_layer(L.Marker(location=location, draggable=False));
        return m


app = App(app_ui, server)
