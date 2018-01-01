### Image ASCIIfy ###

><b>proposition</b><br/>
>Create images for standard consoles by converting the image to ASCII characters.

><b>features</b><br/>
>Invert, Scale ASCII output, export to files, custom tone palettes.

><b>limitations</b><br/>
>Only output greyscale image (toned according to chars in tone-scale).

#### Prerequisites ####

Build in Python 3.6 and makes use of :

<ul>Pillow (PIL), getopt and sys</ul>

#### Quick start ####

The program requires one parameter namely the name of the image you want to Asciify

`> python3.6 imageasciify skull.jpg`

will provide you with the following

```
                     ....... .                              
                ..:!!!!!!!!!!!::::..                        
             .:!cccccoCCoooCoc:::!::::.                     
          :cccoooCCooCooooooooc!::::!!!:.                   
        .!oCCCCCOOOOCCCCoooccc!c!::::::!:.                  
      .!oCCOCOO88OO88888OCo!c!cocccoo!!::::.                
     :coCCCOCCO888O8888O88CCCc!!..:!coo!c::::.              
   .!ooCOOOOOOO88888O8OOCO8Oc.     .:!cc!.   .:             
  .coCC888OOO888OOOCCCocCOo:.     .:coooc!c!. ::            
 .coCCO88OOOOOO8OOCCco!o8Co:      .!oCooCCo:..::            
 :coCOOOOOOCOO88OOCocccCOCCC:     .!cocoOC:  ..:            
 :cco888OCCCOOOCooocc!!oCOCCC!:..:!cCCccCo.  .:..           
 :!!oO88CCOOOCCooccc!:!!oOOOCCoooooo!!ccco:.  !!!!:.        
 :!!oOOCCCCCCCoocccco:.!OOOOOoccc!cc!!cc!c!!..:c!cc!        
 .:ooCCCCCCCo!!!!!ccoooO8OOOCooc!ccoocoOCocccooc!cc!.       
  :!ccooCooc::!:cCOOooo!!!!!!!:...:!oooOOCoccoCo!!:         
  ..:!!ccoc!!!!cOCc:.:.   .. .c!...!oooCOOOCccocc::!.       
   :::c!!coocCCCOc:  .    !Cc.co!!!CCOOCOOCoCco!c!:!!.      
   .::!cccooco!:!!:.      :Co:.o:!oOOCCcCCC!c::...  ..      
    .:.!CCCC!:..:ococ.    oCcc..::cOocOc!:.                 
     .::!!cooooooCccOCoc!oCCoo!  :cOo!:...      .:!::::!.   
      ..:!!cCOOoo!:.!Coocooocoo: ...    ...:.!.!!:c:!!!::   
         :c!!cc!!cc. !ococoooCCC!  :o::c::oc:!:!:::::!!::   
           ..  ..::   cCCooooooCCoccc!!o!coc!:::::::!!!!:   
                       oCCCoco!coooCCoocoo!!::::::::::!!..  
                       :CCoccc!!ooooc!c!c!!:::::::::::::::.
                       .oc!ccooooc!:::!!!!!!::::::::!::....
                        ..!cc!c:..   ................       
                          ..                                
```

You can set a number of settings:

 * reverse tones
 * height and width of ASCII representation
 * the characters making it out for the tones
 * maximize contrast
 * filename for exporting to file
 * using a slower average algorithm

You can see all the settings by

`> python3.6 imageasciify.py -h`

#### Methodology ####

Initially the image is converted to grey scale.
Then the image is partioned into a grid of cells and the program calculates the light itensity for each of these cells. This can be achieve via two methods:
 * Scale down image size so it equals the number of cells in height and width of ASCII output
 * Calculate the average light intensity of each cell (quadrant) the unscaled image

Each method outputs light intensity for each cell, which are then mapped to  the range of characters used to represent different tones of the image. The default grey tone palette is:

<center>  .:!coCO8@ </center>
