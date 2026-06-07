import pandas as pd
import plotly.express as px

# Datos de prueba
df = pd.DataFrame({
    "mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
    "usuarios": [1200000, 1350000, 1280000, 1500000, 1620000, 1700000]
})

color_naranja = "#F37021"
color_fondo = "#0B0B0B"
color_grafica = "#111111"
color_texto = "#FFFFFF"

fig = px.line(
    df,
    x="mes",
    y="usuarios",
    markers=True,
    title="Prueba de gráfica interactiva Plotly"
)

fig.update_traces(
    line=dict(color=color_naranja, width=4),
    marker=dict(color=color_naranja, size=9)
)

fig.update_layout(
    plot_bgcolor=color_grafica,
    paper_bgcolor=color_fondo,
    font=dict(color=color_texto, family="Arial"),
    title_x=0.5,
    xaxis_title="Mes",
    yaxis_title="Usuarios"
)

fig.write_html(
    "grafica_metro.html",
    include_plotlyjs="cdn",
    full_html=True
)

print("Listo: se creó grafica_metro.html")