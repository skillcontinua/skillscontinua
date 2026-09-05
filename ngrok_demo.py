from pyngrok import ngrok
import os
print("Starting public tunnel for ABIAPOLY demo...")
public_url = ngrok.connect(8000, bind_tls=True)
print(f"ABIAPOLY CAN NOW VIEW: {public_url}/en/pillars/")
print(f"ENERGY PILLAR: {public_url}/en/pillars/energy-power-offgrid/")
print("Keep this window OPEN - Don't close!")
input("Press Enter to stop...")