import time
import max7219.led as led

device = led.matrix(cascaded=4)

device.orientation(90)

print 'Press Ctrl+C to stop'

#Bril normaal / Normal bril

try: 
    while True:
        device.brightness(8)
        
        device.pixel(4,0,1)
        device.pixel(5,0,1)
        device.pixel(6,0,1)
        device.pixel(7,0,1)
        device.pixel(8,0,1)
        device.pixel(9,0,1)
        device.pixel(10,0,1)
        device.pixel(11,0,1)
        device.pixel(12,0,1)
        device.pixel(13,0,1)
        device.pixel(18,0,1)
        device.pixel(19,0,1)
        device.pixel(20,0,1)
        device.pixel(21,0,1)
        device.pixel(22,0,1)
        device.pixel(23,0,1)
        device.pixel(24,0,1)
        device.pixel(25,0,1)
        device.pixel(26,0,1)
        device.pixel(27,0,1)
        device.pixel(4,1,1)
        device.pixel(14,1,1)
        device.pixel(17,1,1)
        device.pixel(27,1,1)
        device.pixel(0,2,1)
        device.pixel(1,2,1)
        device.pixel(2,2,1)
        device.pixel(3,2,1)
        device.pixel(14,2,1)
        device.pixel(15,2,1)
        device.pixel(16,2,1)
        device.pixel(17,2,1)
        device.pixel(28,2,1)
        device.pixel(29,2,1)
        device.pixel(30,2,1)
        device.pixel(31,2,1)
        device.pixel(3,3,1)
        device.pixel(8,3,1)
        device.pixel(9,3,1)
        device.pixel(14,3,1)
        device.pixel(15,3,1)
        device.pixel(16,3,1)
        device.pixel(17,3,1)
        device.pixel(22,3,1)
        device.pixel(23,3,1)
        device.pixel(28,3,1)
        device.pixel(3,4,1)
        device.pixel(8,4,1)
        device.pixel(9,4,1)
        device.pixel(14,4,1)
        device.pixel(17,4,1)
        device.pixel(22,4,1)
        device.pixel(23,4,1)
        device.pixel(28,4,1)
        device.pixel(3,5,1)
        device.pixel(13,5,1)
        device.pixel(18,5,1)
        device.pixel(28,5,1)
        device.pixel(4,6,1)
        device.pixel(12,6,1)
        device.pixel(19,6,1)
        device.pixel(27,6,1)
        device.pixel(5,7,1)
        device.pixel(6,7,1)
        device.pixel(7,7,1)
        device.pixel(8,7,1)
        device.pixel(9,7,1)
        device.pixel(10,7,1)
        device.pixel(11,7,1)
        device.pixel(20,7,1)
        device.pixel(21,7,1)
        device.pixel(22,7,1)
        device.pixel(23,7,1)
        device.pixel(24,7,1)
        device.pixel(25,7,1)
        device.pixel(26,7,1)
        time.sleep(5)

#naar links kijken
        
        #linkeroog						
        device.pixel(9,3,0)						
        device.pixel(9,4,0)						
        device.pixel(7,4,1)						
        device.pixel(7,3,1)
        
                                                        
        #rechteroog						
        device.pixel(23,3,0)						
        device.pixel(23,4,0)						
        device.pixel(21,4,1)						
        device.pixel(21,3,1)						
        time.sleep(0.1)

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(8,4,0)
        device.pixel(6,4,1)
        device.pixel(6,3,1)

        #rechteroog
        device.pixel(22,3,0)
        device.pixel(22,4,0)
        device.pixel(20,4,1)
        device.pixel(20,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(7,3,0)
        device.pixel(7,4,0)
        device.pixel(5,4,1)
        device.pixel(5,3,1)

        #rechteroog
        device.pixel(21,3,0)
        device.pixel(21,4,0)
        device.pixel(19,4,1)
        device.pixel(19,3,1)
        time.sleep(2)

       # ….en weer terug						

        #linkeroog
        device.pixel(5,3,0)
        device.pixel(5,4,0)
        device.pixel(7,4,1)
        device.pixel(7,3,1)

        #rechteroog
        device.pixel(19,3,0)
        device.pixel(19,4,0)
        device.pixel(21,4,1)
        device.pixel(21,3,1)
        time.sleep(0.1)

				
        #linkeroog						
        device.pixel(6,3,0)						
        device.pixel(6,4,0)						
        device.pixel(8,4,1)						
        device.pixel(8,3,1)
                                                                
        #rechteroog						
        device.pixel(20,3,0)						
        device.pixel(20,4,0)						
        device.pixel(22,4,1)						
        device.pixel(22,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(7,3,0)
        device.pixel(7,4,0)
        device.pixel(9,4,1)
        device.pixel(9,3,1)

        #rechteroog
        device.pixel(21,3,0)
        device.pixel(21,4,0)
        device.pixel(23,4,1)
        device.pixel(23,3,1)

# Naar rechts kijken

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(8,4,0)
        device.pixel(10,3,1)
        device.pixel(10,4,1)

        #rechteroog
        device.pixel(22,3,0)
        device.pixel(22,4,0)
        device.pixel(24,3,1)
        device.pixel(24,4,1)
        time.sleep(0.1)


        #linkeroog
        device.pixel(9,3,0)
        device.pixel(9,4,0)
        device.pixel(11,3,1)
        device.pixel(11,4,1)

        #rechteroog
        device.pixel(23,3,0)
        device.pixel(23,4,0)
        device.pixel(25,3,1)
        device.pixel(25,4,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(10,3,0)
        device.pixel(10,4,0)
        device.pixel(12,3,1)
        device.pixel(12,4,1)

        #rechteroog
        device.pixel(24,3,0)
        device.pixel(24,4,0)
        device.pixel(26,3,1)
        device.pixel(26,4,1)
        time.sleep(2)

        # En weer terug..
        #linkeroog
        device.pixel(12,3,0)
        device.pixel(12,4,0)
        device.pixel(10,3,1)
        device.pixel(10,4,1)

        #rechteroog
        device.pixel(26,3,0)
        device.pixel(26,4,0)
        device.pixel(24,3,1)
        device.pixel(24,4,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(11,3,0)
        device.pixel(11,4,0)
        device.pixel(9,3,1)
        device.pixel(9,4,1)

        #rechteroog
        device.pixel(25,3,0)
        device.pixel(25,4,0)
        device.pixel(23,3,1)
        device.pixel(23,4,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(10,3,0)
        device.pixel(10,4,0)
        device.pixel(8,3,1)
        device.pixel(8,4,1)

        #rechteroog
        device.pixel(24,3,0)
        device.pixel(24,4,0)
        device.pixel(22,3,1)
        device.pixel(22,4,1)
        time.sleep(3)

# Knipperen

        #Dicht

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(9,3,0)
        device.pixel(7,4,1)


        #rechteroog
        device.pixel(22,3,0)
        device.pixel(23,3,0)
        device.pixel(24,4,1)
        time.sleep(0.1)

        # En weer open..

        #linkeroog
        device.pixel(7,4,0)
        device.pixel(8,3,1)
        device.pixel(9,3,1)


        #rechteroog
        device.pixel(24,4,0)
        device.pixel(22,3,1)
        device.pixel(23,3,1)
        time.sleep(0.5)

        # Weer dicht

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(9,3,0)
        device.pixel(7,4,1)


        #rechteroog
        device.pixel(22,3,0)
        device.pixel(23,3,0)
        device.pixel(24,4,1)
        time.sleep(0.1)

        # En weer open..

        #linkeroog
        device.pixel(7,4,0)
        device.pixel(8,3,1)
        device.pixel(9,3,1)


        #rechteroog
        device.pixel(24,4,0)
        device.pixel(22,3,1)
        device.pixel(23,3,1)
        time.sleep(3)

# Scheel kijken

       #linkeroog
        device.pixel(8,3,0)
        device.pixel(8,4,0)
        device.pixel(10,3,1)
        device.pixel(10,4,1)

        #rechteroog
        device.pixel(23,3,0)
        device.pixel(23,4,0)
        device.pixel(21,4,1)
        device.pixel(21,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(9,3,0)
        device.pixel(9,4,0)
        device.pixel(11,3,1)
        device.pixel(11,4,1)

        #rechteroog
        device.pixel(22,3,0)
        device.pixel(22,4,0)
        device.pixel(20,4,1)
        device.pixel(20,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(10,3,0)
        device.pixel(10,4,0)
        device.pixel(12,3,1)
        device.pixel(12,4,1)

        #rechteroog
        device.pixel(21,3,0)
        device.pixel(21,4,0)
        device.pixel(19,4,1)
        device.pixel(19,3,1)
        time.sleep(2.5)

        # En weer terug...
        
        #linkeroog
        device.pixel(12,3,0)
        device.pixel(12,4,0)
        device.pixel(10,3,1)
        device.pixel(10,4,1)


        #rechteroog
        device.pixel(19,3,0)
        device.pixel(19,4,0)
        device.pixel(21,4,1)
        device.pixel(21,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(11,3,0)
        device.pixel(11,4,0)
        device.pixel(9,3,1)
        device.pixel(9,4,1)

        #rechteroog
        device.pixel(20,3,0)
        device.pixel(20,4,0)
        device.pixel(22,4,1)
        device.pixel(22,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(10,3,0)
        device.pixel(10,4,0)
        device.pixel(8,3,1)
        device.pixel(8,4,1)

        #rechteroog
        device.pixel(21,3,0)
        device.pixel(21,4,0)
        device.pixel(23,4,1)
        device.pixel(23,3,1)
        time.sleep(5)


#Oog eenvoudig

        device.clear()
        device.pixel(5,0,1)
        device.pixel(6,0,1)
        device.pixel(7,0,1)
        device.pixel(8,0,1)
        device.pixel(9,0,1)
        device.pixel(10,0,1)
        device.pixel(11,0,1)
        device.pixel(12,0,1)
        device.pixel(17,0,1)
        device.pixel(19,0,1)
        device.pixel(20,0,1)
        device.pixel(21,0,1)
        device.pixel(22,0,1)
        device.pixel(23,0,1)
        device.pixel(24,0,1)
        device.pixel(4,1,1)
        device.pixel(5,1,1)
        device.pixel(13,1,1)
        device.pixel(16,1,1)
        device.pixel(17,1,1)
        device.pixel(25,1,1)
        device.pixel(4,2,1)
        device.pixel(14,2,1)
        device.pixel(16,2,1)
        device.pixel(26,2,1)
        device.pixel(4,3,1)
        device.pixel(8,3,1)
        device.pixel(9,3,1)
        device.pixel(15,3,1)
        device.pixel(16,3,1)
        device.pixel(22,3,1)
        device.pixel(23,3,1)
        device.pixel(27,3,1)
        device.pixel(4,4,1)
        device.pixel(8,4,1)
        device.pixel(9,4,1)
        device.pixel(16,4,1)
        device.pixel(22,4,1)
        device.pixel(23,4,1)
        device.pixel(28,4,1)
        device.pixel(4,5,1)
        device.pixel(16,5,1)
        device.pixel(28,5,1)
        device.pixel(4,6,1)
        device.pixel(16,6,1)
        device.pixel(28,6,1)
        device.pixel(4,7,1)
        device.pixel(5,7,1)
        device.pixel(6,7,1)
        device.pixel(7,7,1)
        device.pixel(8,7,1)
        device.pixel(9,7,1)
        device.pixel(10,7,1)
        device.pixel(11,7,1)
        device.pixel(12,7,1)
        device.pixel(13,7,1)
        device.pixel(14,7,1)
        device.pixel(15,7,1)
        device.pixel(16,7,1)
        device.pixel(17,7,1)
        device.pixel(18,7,1)
        device.pixel(19,7,1)
        device.pixel(20,7,1)
        device.pixel(21,7,1)
        device.pixel(22,7,1)
        device.pixel(23,7,1)
        device.pixel(24,7,1)
        device.pixel(25,7,1)
        device.pixel(26,7,1)
        device.pixel(27,7,1)
        device.pixel(28,7,1)
        time.sleep(5)

    # Scheel kijken

       #linkeroog
        device.pixel(8,3,0)
        device.pixel(8,4,0)
        device.pixel(10,3,1)
        device.pixel(10,4,1)

        #rechteroog
        device.pixel(23,3,0)
        device.pixel(23,4,0)
        device.pixel(21,4,1)
        device.pixel(21,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(9,3,0)
        device.pixel(9,4,0)
        device.pixel(11,3,1)
        device.pixel(11,4,1)

        #rechteroog
        device.pixel(22,3,0)
        device.pixel(22,4,0)
        device.pixel(20,4,1)
        device.pixel(20,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(10,3,0)
        device.pixel(10,4,0)
        device.pixel(12,3,1)
        device.pixel(12,4,1)

        #rechteroog
        device.pixel(21,3,0)
        device.pixel(21,4,0)
        device.pixel(19,4,1)
        device.pixel(19,3,1)
        time.sleep(2.5)

        # En weer terug...
        
        #linkeroog
        device.pixel(12,3,0)
        device.pixel(12,4,0)
        device.pixel(10,3,1)
        device.pixel(10,4,1)


        #rechteroog
        device.pixel(19,3,0)
        device.pixel(19,4,0)
        device.pixel(21,4,1)
        device.pixel(21,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(11,3,0)
        device.pixel(11,4,0)
        device.pixel(9,3,1)
        device.pixel(9,4,1)

        #rechteroog
        device.pixel(20,3,0)
        device.pixel(20,4,0)
        device.pixel(22,4,1)
        device.pixel(22,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(10,3,0)
        device.pixel(10,4,0)
        device.pixel(8,3,1)
        device.pixel(8,4,1)

        #rechteroog
        device.pixel(21,3,0)
        device.pixel(21,4,0)
        device.pixel(23,4,1)
        device.pixel(23,3,1)
        time.sleep(5)

    # Knipperen

        #Dicht

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(9,3,0)
        device.pixel(7,4,1)


        #rechteroog
        device.pixel(22,3,0)
        device.pixel(23,3,0)
        device.pixel(24,4,1)
        time.sleep(0.1)

        # En weer open..

        #linkeroog
        device.pixel(7,4,0)
        device.pixel(8,3,1)
        device.pixel(9,3,1)


        #rechteroog
        device.pixel(24,4,0)
        device.pixel(22,3,1)
        device.pixel(23,3,1)
        time.sleep(0.5)

        # Weer dicht

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(9,3,0)
        device.pixel(7,4,1)


        #rechteroog
        device.pixel(22,3,0)
        device.pixel(23,3,0)
        device.pixel(24,4,1)
        time.sleep(0.1)

        # En weer open..

        #linkeroog
        device.pixel(7,4,0)
        device.pixel(8,3,1)
        device.pixel(9,3,1)


        #rechteroog
        device.pixel(24,4,0)
        device.pixel(22,3,1)
        device.pixel(23,3,1)
        time.sleep(3)


    #naar links kijken
        
        #linkeroog						
        device.pixel(9,3,0)						
        device.pixel(9,4,0)						
        device.pixel(7,4,1)						
        device.pixel(7,3,1)
        
                                                        
        #rechteroog						
        device.pixel(23,3,0)						
        device.pixel(23,4,0)						
        device.pixel(21,4,1)						
        device.pixel(21,3,1)						
        time.sleep(0.1)

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(8,4,0)
        device.pixel(6,4,1)
        device.pixel(6,3,1)

        #rechteroog
        device.pixel(22,3,0)
        device.pixel(22,4,0)
        device.pixel(20,4,1)
        device.pixel(20,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(7,3,0)
        device.pixel(7,4,0)
        device.pixel(5,4,1)
        device.pixel(5,3,1)

        #rechteroog
        device.pixel(21,3,0)
        device.pixel(21,4,0)
        device.pixel(19,4,1)
        device.pixel(19,3,1)
        time.sleep(2)

       # ….en weer terug						

        #linkeroog
        device.pixel(5,3,0)
        device.pixel(5,4,0)
        device.pixel(7,4,1)
        device.pixel(7,3,1)

        #rechteroog
        device.pixel(19,3,0)
        device.pixel(19,4,0)
        device.pixel(21,4,1)
        device.pixel(21,3,1)
        time.sleep(0.1)

				
        #linkeroog						
        device.pixel(6,3,0)						
        device.pixel(6,4,0)						
        device.pixel(8,4,1)						
        device.pixel(8,3,1)
                                                                
        #rechteroog						
        device.pixel(20,3,0)						
        device.pixel(20,4,0)						
        device.pixel(22,4,1)						
        device.pixel(22,3,1)
        time.sleep(0.1)

        #linkeroog
        device.pixel(7,3,0)
        device.pixel(7,4,0)
        device.pixel(9,4,1)
        device.pixel(9,3,1)

        #rechteroog
        device.pixel(21,3,0)
        device.pixel(21,4,0)
        device.pixel(23,4,1)
        device.pixel(23,3,1)

    # Knipperen

        #Dicht

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(9,3,0)
        device.pixel(7,4,1)


        #rechteroog
        device.pixel(22,3,0)
        device.pixel(23,3,0)
        device.pixel(24,4,1)
        time.sleep(0.1)

        # En weer open..

        #linkeroog
        device.pixel(7,4,0)
        device.pixel(8,3,1)
        device.pixel(9,3,1)


        #rechteroog
        device.pixel(24,4,0)
        device.pixel(22,3,1)
        device.pixel(23,3,1)
        time.sleep(0.5)

        # Weer dicht

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(9,3,0)
        device.pixel(7,4,1)


        #rechteroog
        device.pixel(22,3,0)
        device.pixel(23,3,0)
        device.pixel(24,4,1)
        time.sleep(0.1)

        # En weer open..

        #linkeroog
        device.pixel(7,4,0)
        device.pixel(8,3,1)
        device.pixel(9,3,1)


        #rechteroog
        device.pixel(24,4,0)
        device.pixel(22,3,1)
        device.pixel(23,3,1)
        time.sleep(3)
      
except KeyboardInterrupt:
    device.clear()
  
    
    
    






