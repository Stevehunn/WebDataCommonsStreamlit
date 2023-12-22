import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import glob
import re


# Version Window
def parseWindow(target_classes):
    for file in glob.glob("assets/plots/*.svg"):
        # Utilisez split pour séparer le chemin du fichier
        parts = file.split("/")

        # Extrait le premier élément après "assets"
        fname = parts[1]  # parts[0] est "assets", parts[1] est "plots"

        parts2 = fname.split("plots")
        # Extrait le premier élément après "plots"
        newFname = parts2[1]

        # Utiliser split pour séparer la chaîne en fonction de "\"
        parts = newFname.split("\\")

        # Concaténer les parties avec "schema:"
        newFname = "".join(parts[1:])

        # Supprime l'extension ".svg"
        cname = newFname.split("_plot.svg")[0]

        # Ajoute à la liste avec le préfixe "schema:"
        target_classes.append(f"schema:{cname}")

# Version Mac
def parseMac(target_classes):
    for file in glob.glob("assets/plots/*.svg"):
        # Utilisez split pour séparer le chemin du fichier
        parts = file.split("/")

        fname = parts[2]
        parts2 = fname.split(".")
        # Extrait le premier élément après "plots"
        newFname =parts2[0]

        cname = newFname.split("_plot")[0]
        if cname != "Intangible":
            target_classes.append(f"schema:{cname}")