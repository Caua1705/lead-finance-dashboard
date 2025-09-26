import streamlit as st
import plotly.express as px

def grafico_evolucao_diaria(df, x, y, cor_linha, titulo, titulo_x, titulo_y):
    fig = px.line(
        df, x, y,
        line_shape="spline", markers=True
    )
    fig.update_traces(line=dict(width=2, color=cor_linha))  

    fig.update_layout(
        title={'text': titulo, 'x': 0.0, 'xanchor': 'left'},
        xaxis_title=titulo_x, yaxis_title=titulo_y,
        plot_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="#E5E7EB", dtick="D1",
                   tickformat="%d/%m", tickangle=-45),
        yaxis=dict(showgrid=True, gridcolor="#E5E7EB"),
        font=dict(color="#111827")
    )
    st.plotly_chart(fig, use_container_width=True)


def grafico_distribuicao_pizza(df, nomes, valores, titulo, mapa_cores):
    fig = px.pie(
        df, names=nomes, values=valores,
        hole=0.4, color=nomes,
        color_discrete_map=mapa_cores
    )
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(
        title={'text': titulo, 'x': 0.0, 'xanchor': 'left'},
        showlegend=True,
        legend=dict(orientation="h", y=-0.2, x=0.5, xanchor="center"),
        font=dict(color="#111827")
    )
    st.plotly_chart(fig, use_container_width=True)


def grafico_distribuicao_barra(df, x, y, titulo, titulo_x, titulo_y, cor):
    fig = px.bar(df, x=x, y=y, text=y)
    fig.update_traces(
        textposition="outside",
        marker_color=cor,
        marker_line=dict(width=0)
    )
    fig.update_layout(
        title={'text': titulo, 'x': 0.0, 'xanchor': 'left'},
        xaxis_title=titulo_x,
        yaxis_title=titulo_y,
        plot_bgcolor="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#E5E7EB"),
        font=dict(color="#111827"),
        uniformtext_minsize=10, uniformtext_mode='hide'
    )
    st.plotly_chart(fig, use_container_width=True)