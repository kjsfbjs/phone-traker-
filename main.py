import requests
import argparse
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import folium
import json
import os
from rich.console import Console
from rich.table import Table

# === Setup Console for CLI Output ===
console = Console()

# === API Configuration ===
API_KEY = "num_live_GZt9YTMwm6YIgPYD6YWw2Ea79639wZEv0qVP4Qnt"  # Replace with your NumLookup API key
HISTORY_FILE = "lookup_history.json"


# === Load or Initialize Lookup History ===
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    return []


def save_history(entry):
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


# === Reverse Social Media Lookup ===
def social_media_lookup(phone):
    """Simulates social media lookup (API access required for real data)."""
    console.print(f"[cyan]🔍 Searching social media for {phone}...[/cyan]")
    return {
        "Facebook": f"https://www.facebook.com/search/top?q={phone}",
        "LinkedIn": f"https://www.linkedin.com/search/results/people/?keywords={phone}",
        "Twitter": f"https://twitter.com/search?q={phone}",
        "Instagram": f"https://www.instagram.com/explore/tags/{phone}/",
        "TikTok": f"https://www.tiktok.com/search?q={phone}"
    }


# === Phone Lookup Function ===
def lookup_number(phone):
    """Fetches phone number details from NumLookup API."""
    url = f"https://api.numlookupapi.com/v1/validate/{phone}?apikey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        table = Table(title="📞 Phone Number Lookup", show_header=True, header_style="bold cyan")
        table.add_column("Field", style="bold", justify="left")
        table.add_column("Details", style="italic", justify="right")

        table.add_row("📌 Phone Number", data.get("international_format", "N/A"))
        table.add_row("📍 Country", data.get("country_name", "N/A"))
        table.add_row("📡 Carrier", data.get("carrier", "N/A"))
        table.add_row("📞 Line Type", data.get("line_type", "N/A"))

        console.print(table)

        # Add Social Media Lookup for CLI
        social_links = social_media_lookup(phone)
        for platform, link in social_links.items():
            console.print(f"[yellow]🔍 {platform}: {link}[/yellow]")

        save_history(data)

        return data
    else:
        console.print("[red]❌ Error: Unable to fetch details. Check API key or phone number.[/red]")
        return None


# === Generate Map Based on Country ===
def generate_map(country_name):
    if not country_name or country_name == "N/A":
        messagebox.showerror("Error", "Location data not available.")
        return
    world_map = folium.Map(location=[20, 0], zoom_start=2)
    folium.Marker(location=[20, 0], popup=f"Carrier Location: {country_name}").add_to(world_map)
    map_file = "phone_location.html"
    world_map.save(map_file)
    webbrowser.open(map_file)


# === GUI Function ===
def gui_lookup():
    phone = phone_entry.get()
    if not phone:
        messagebox.showerror("Error", "Please enter a phone number!")
        return

    data = lookup_number(phone)
    if data:
        country_name = data.get('country_name', 'N/A')
        result_text.set(
            f"📌 Phone: {data.get('international_format', 'N/A')}\n"
            f"📍 Country: {country_name}\n"
            f"📡 Carrier: {data.get('carrier', 'N/A')}\n"
            f"📞 Line Type: {data.get('line_type', 'N/A')}"
        )

        social_links = social_media_lookup(phone)
        social_text.set("\n".join([f"🔍 {platform}: {link}" for platform, link in social_links.items()]))

        view_map_button.config(state="normal", command=lambda: generate_map(country_name))
    else:
        messagebox.showerror("Error", "Failed to retrieve details.")


# === GUI Setup ===
app = tk.Tk()
app.title("Phone Lookup by Sahil")
app.geometry("450x500")
app.config(bg="#1e1e1e")

try:
    icon_img = Image.open("phone_icon.png").resize((60, 60))
except FileNotFoundError:
    icon_img = Image.new("RGB", (60, 60), color="gray")  # Placeholder image
icon_photo = ImageTk.PhotoImage(icon_img)

tk.Label(app, image=icon_photo, bg="#1e1e1e").pack(pady=5)
tk.Label(app, text="Phone Lookup by Sahil", font=("Arial", 14, "bold"), bg="#1e1e1e", fg="cyan").pack(pady=5)
tk.Label(app, text="Enter Phone Number:", font=("Arial", 12), bg="#1e1e1e", fg="white").pack()
phone_entry = tk.Entry(app, font=("Arial", 14), width=20)
phone_entry.pack(pady=5)
tk.Button(app, text="Lookup", font=("Arial", 12), bg="cyan", fg="black", command=gui_lookup).pack(pady=10)
result_text = tk.StringVar()
tk.Label(app, textvariable=result_text, font=("Arial", 12), wraplength=400, bg="#1e1e1e", fg="white").pack()
social_text = tk.StringVar()
tk.Label(app, textvariable=social_text, font=("Arial", 10), wraplength=400, bg="#1e1e1e", fg="yellow").pack()
view_map_button = tk.Button(app, text="View on Map", font=("Arial", 12), bg="green", fg="white", state="disabled")
view_map_button.pack(pady=5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lookup phone number details using NumLookup API")
    parser.add_argument("--cli", type=str, help="Enter the phone number to lookup (e.g., +11234567890)")
    args = parser.parse_args()
    if args.cli:
        lookup_number(args.cli)
    else:
        app.mainloop()
