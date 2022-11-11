import urllib.request
import os 
import pathlib



pathlib.Path(f"Sonidos habbo").mkdir(parents=True, exist_ok=True)
os.chdir(os.path.join(os.getcwd(),f"Sonidos habbo")) 


totalSonidos=0
for i in range(1,737):
    totalSonidos=totalSonidos+1
   
    DescargarSonido = open(f'sound_sample_{i}.mp3','wb')

    print(f"Descargando-> https://images.habbo.com/dcr/hof_furni/mp3/sound_machine_sample_{i}.mp3")
    
    DescargarSonido.write(urllib.request.urlopen(f'https://images.habbo.com/dcr/hof_furni/mp3/sound_machine_sample_{i}.mp3').read())
    
    DescargarSonido.close()
print(f"Se han descargado un total de {totalSonidos} sonidos.")

