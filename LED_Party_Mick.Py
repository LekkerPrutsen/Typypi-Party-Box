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

       # ...en weer terug						

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


# Draaien met de ogen

        #linkeroog
        device.pixel(8,3,0)
        device.pixel(9,3,0)
        device.pixel(8,5,1)
        device.pixel(9,5,1)

        for i in range(3):

            #rechteroog
            device.pixel(22,3,0)
            device.pixel(23,3,0)
            device.pixel(22,5,1)
            device.pixel(23,5,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(9,4,0)
            device.pixel(9,5,0)
            device.pixel(7,4,1)
            device.pixel(7,5,1)

            #rechteroog
            device.pixel(22,4,0)
            device.pixel(22,5,0)
            device.pixel(24,4,1)
            device.pixel(24,5,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(8,4,0)
            device.pixel(8,5,0)
            device.pixel(6,4,1)
            device.pixel(6,5,1)

            #rechteroog
            device.pixel(23,4,0)
            device.pixel(23,5,0)
            device.pixel(25,4,1)
            device.pixel(25,5,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(6,5,0)
            device.pixel(7,5,0)
            device.pixel(6,3,1)
            device.pixel(7,3,1)

            #rechteroog
            device.pixel(24,5,0)
            device.pixel(25,5,0)
            device.pixel(24,3,1)
            device.pixel(25,3,1)
            time.sleep(0.1)

            
            #linkeroog
            device.pixel(6,4,0)
            device.pixel(7,4,0)
            device.pixel(6,2,1)
            device.pixel(7,2,1)

            #rechteroog
            device.pixel(24,4,0)
            device.pixel(25,4,0)
            device.pixel(24,2,1)
            device.pixel(25,2,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(6,2,0)
            device.pixel(6,3,0)
            device.pixel(8,2,1)
            device.pixel(8,3,1)

            #rechteroog
            device.pixel(25,2,0)
            device.pixel(25,3,0)
            device.pixel(23,2,1)
            device.pixel(23,3,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(7,2,0)
            device.pixel(7,3,0)
            device.pixel(9,2,1)
            device.pixel(9,3,1)

            #rechteroog
            device.pixel(24,2,0)
            device.pixel(24,3,0)
            device.pixel(22,2,1)
            device.pixel(22,3,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(8,2,0)
            device.pixel(8,3,0)
            device.pixel(10,2,1)
            device.pixel(10,3,1)

            #rechteroog
            device.pixel(23,2,0)
            device.pixel(23,3,0)
            device.pixel(21,2,1)
            device.pixel(21,3,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(9,2,0)
            device.pixel(9,3,0)
            device.pixel(11,2,1)
            device.pixel(11,3,1)

            #rechteroog
            device.pixel(22,2,0)
            device.pixel(22,3,0)
            device.pixel(20,2,1)
            device.pixel(20,3,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(10,2,0)
            device.pixel(11,2,0)
            device.pixel(10,4,1)
            device.pixel(11,4,1)

            #rechteroog
            device.pixel(21,2,0)
            device.pixel(20,2,0)
            device.pixel(20,4,1)
            device.pixel(21,4,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(10,3,0)
            device.pixel(11,3,0)
            device.pixel(10,5,1)
            device.pixel(11,5,1)

            #rechteroog
            device.pixel(21,3,0)
            device.pixel(20,3,0)
            device.pixel(20,5,1)
            device.pixel(21,5,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(11,4,0)
            device.pixel(11,5,0)
            device.pixel(9,4,1)
            device.pixel(9,5,1)

            #rechteroog
            device.pixel(20,4,0)
            device.pixel(20,5,0)
            device.pixel(22,4,1)
            device.pixel(22,5,1)
            time.sleep(0.1)

            #linkeroog
            device.pixel(10,4,0)
            device.pixel(10,5,0)
            device.pixel(8,4,1)
            device.pixel(8,5,1)

            #rechteroog
            device.pixel(21,4,0)
            device.pixel(21,5,0)
            device.pixel(23,4,1)
            device.pixel(23,5,1)
            time.sleep(0.1)

        #...en weer terug naar het midden

        #linkeroog
        device.pixel(8,5,0)
        device.pixel(9,5,0)
        device.pixel(8,3,1)
        device.pixel(9,3,1)

        #rechteroog
        device.pixel(22,5,0)
        device.pixel(23,5,0)
        device.pixel(23,3,1)
        device.pixel(22,3,1)
        time.sleep(0.1)

        device.clear()

        time.sleep(2)

        #ASCII codes 
        symbol01 = 219
        symbol02 = 178
        symbol03 = 177
        symbol04 = 176

        duration = 0.2

        #position 1
        device.letter(0, symbol01)
        device.letter(1, symbol02)
        device.letter(2, symbol04)
        device.letter(3, symbol04)
        time.sleep(duration)

        #position 2
        device.letter(0, symbol02)
        device.letter(1, symbol01)
        device.letter(2, symbol04)
        device.clear(3)
        time.sleep(duration)

        #position 3
        device.letter(0, symbol03)
        device.letter(1, symbol02)
        device.letter(2, symbol01)
        device.clear(3)
        time.sleep(duration)

        #position 4
        device.letter(0, symbol04)
        device.letter(1, symbol03)
        device.letter(2, symbol02)
        device.letter(3, symbol01)
        time.sleep(duration)

        #position 5
        device.clear(0)
        device.letter(1, symbol04)
        device.letter(2, symbol01)
        device.letter(3, symbol02)
        time.sleep(duration)
        
        #position 6
        device.clear(0)
        device.letter(1, symbol01)
        device.letter(2, symbol02)
        device.letter(3, symbol03)
        time.sleep(duration)

        #position 1
        device.letter(0, symbol01)
        device.letter(1, symbol02)
        device.letter(2, symbol04)
        device.letter(3, symbol04)
        time.sleep(duration)

        #position 2
        device.letter(0, symbol02)
        device.letter(1, symbol01)
        device.letter(2, symbol04)
        device.clear(3)
        time.sleep(duration)

        #position 3
        device.letter(0, symbol03)
        device.letter(1, symbol02)
        device.letter(2, symbol01)
        device.clear(3)
        time.sleep(duration)

        #position 4
        device.letter(0, symbol04)
        device.letter(1, symbol03)
        device.letter(2, symbol02)
        device.letter(3, symbol01)
        time.sleep(duration)

        #position 5
        device.clear(0)
        device.letter(1, symbol04)
        device.letter(2, symbol01)
        device.letter(3, symbol02)
        time.sleep(duration)
        
        #position 6
        device.clear(0)
        device.letter(1, symbol01)
        device.letter(2, symbol02)
        device.letter(3, symbol03)
        time.sleep(duration)

        #position 1
        device.letter(0, symbol01)
        device.letter(1, symbol02)
        device.letter(2, symbol04)
        device.letter(3, symbol04)
        time.sleep(duration)

        #position 2
        device.letter(0, symbol02)
        device.letter(1, symbol01)
        device.letter(2, symbol04)
        device.clear(3)
        time.sleep(duration)

        #position 3
        device.letter(0, symbol03)
        device.letter(1, symbol02)
        device.letter(2, symbol01)
        device.clear(3)
        time.sleep(duration)

        #position 4
        device.letter(0, symbol04)
        device.letter(1, symbol03)
        device.letter(2, symbol02)
        device.letter(3, symbol01)
        time.sleep(duration)

        #position 5
        device.clear(0)
        device.letter(1, symbol04)
        device.letter(2, symbol01)
        device.letter(3, symbol02)
        time.sleep(duration)
        
        #position 6
        device.clear(0)
        device.letter(1, symbol01)
        device.letter(2, symbol02)
        device.letter(3, symbol03)
        time.sleep(duration)

        #position 1
        device.letter(0, symbol01)
        device.letter(1, symbol02)
        device.letter(2, symbol04)
        device.letter(3, symbol04)
        time.sleep(duration)

        #position 2
        device.letter(0, symbol02)
        device.letter(1, symbol01)
        device.letter(2, symbol04)
        device.clear(3)
        time.sleep(duration)

        #position 3
        device.letter(0, symbol03)
        device.letter(1, symbol02)
        device.letter(2, symbol01)
        device.clear(3)
        time.sleep(duration)

        #position 4
        device.letter(0, symbol04)
        device.letter(1, symbol03)
        device.letter(2, symbol02)
        device.letter(3, symbol01)
        time.sleep(duration)

        #position 5
        device.clear(0)
        device.letter(1, symbol04)
        device.letter(2, symbol01)
        device.letter(3, symbol02)
        time.sleep(duration)
        
        #position 6
        device.clear(0)
        device.letter(1, symbol01)
        device.letter(2, symbol02)
        device.letter(3, symbol03)
        time.sleep(1)


        device.clear()

        device.show_message("PARTY TIME @ MICK'S PLACE !!!")
        time.sleep(2)
        device.show_message("WELCOME TO GROUP 8A")
        time.sleep(2)

        #ASCII codes 
        symbol01 = 219
        symbol02 = 240
        symbol03 = 45
        symbol04 = 32

        duration = 0.2

        #position 1
        device.letter(0, symbol01)
        device.letter(1, symbol02)
        device.letter(2, symbol04)
        device.letter(3, symbol04)
        time.sleep(duration)

        #position 2
        device.letter(0, symbol02)
        device.letter(1, symbol01)
        device.letter(2, symbol04)
        device.clear(3)
        time.sleep(duration)

        #position 3
        device.letter(0, symbol03)
        device.letter(1, symbol02)
        device.letter(2, symbol01)
        device.clear(3)
        time.sleep(duration)

        #position 4
        device.letter(0, symbol04)
        device.letter(1, symbol03)
        device.letter(2, symbol02)
        device.letter(3, symbol01)
        time.sleep(duration)

        #position 5
        device.clear(0)
        device.letter(1, symbol04)
        device.letter(2, symbol01)
        device.letter(3, symbol02)
        time.sleep(duration)
        
        #position 6
        device.clear(0)
        device.letter(1, symbol01)
        device.letter(2, symbol02)
        device.letter(3, symbol03)
        time.sleep(duration)

        #position 1
        device.letter(0, symbol01)
        device.letter(1, symbol02)
        device.letter(2, symbol04)
        device.letter(3, symbol04)
        time.sleep(duration)

        #position 2
        device.letter(0, symbol02)
        device.letter(1, symbol01)
        device.letter(2, symbol04)
        device.clear(3)
        time.sleep(duration)

        #position 3
        device.letter(0, symbol03)
        device.letter(1, symbol02)
        device.letter(2, symbol01)
        device.clear(3)
        time.sleep(duration)

        #position 4
        device.letter(0, symbol04)
        device.letter(1, symbol03)
        device.letter(2, symbol02)
        device.letter(3, symbol01)
        time.sleep(duration)

        #position 5
        device.clear(0)
        device.letter(1, symbol04)
        device.letter(2, symbol01)
        device.letter(3, symbol02)
        time.sleep(duration)
        
        #position 6
        device.clear(0)
        device.letter(1, symbol01)
        device.letter(2, symbol02)
        device.letter(3, symbol03)
        time.sleep(duration)

         #position 1
        device.letter(0, symbol01)
        device.letter(1, symbol02)
        device.letter(2, symbol04)
        device.letter(3, symbol04)
        time.sleep(duration)

        #position 2
        device.letter(0, symbol02)
        device.letter(1, symbol01)
        device.letter(2, symbol04)
        device.clear(3)
        time.sleep(duration)

        #position 3
        device.letter(0, symbol03)
        device.letter(1, symbol02)
        device.letter(2, symbol01)
        device.clear(3)
        time.sleep(duration)

        #position 4
        device.letter(0, symbol04)
        device.letter(1, symbol03)
        device.letter(2, symbol02)
        device.letter(3, symbol01)
        time.sleep(duration)

        #position 5
        device.clear(0)
        device.letter(1, symbol04)
        device.letter(2, symbol01)
        device.letter(3, symbol02)
        time.sleep(duration)
        
        #position 6
        device.clear(0)
        device.letter(1, symbol01)
        device.letter(2, symbol02)
        device.letter(3, symbol03)
        time.sleep(duration)

        #position 1
        device.letter(0, symbol01)
        device.letter(1, symbol02)
        device.letter(2, symbol04)
        device.letter(3, symbol04)
        time.sleep(duration)

        #position 2
        device.letter(0, symbol02)
        device.letter(1, symbol01)
        device.letter(2, symbol04)
        device.clear(3)
        time.sleep(duration)

        #position 3
        device.letter(0, symbol03)
        device.letter(1, symbol02)
        device.letter(2, symbol01)
        device.clear(3)
        time.sleep(duration)

        #position 4
        device.letter(0, symbol04)
        device.letter(1, symbol03)
        device.letter(2, symbol02)
        device.letter(3, symbol01)
        time.sleep(duration)

        #position 5
        device.clear(0)
        device.letter(1, symbol04)
        device.letter(2, symbol01)
        device.letter(3, symbol02)
        time.sleep(duration)
        
        #position 6
        device.clear(0)
        device.letter(1, symbol01)
        device.letter(2, symbol02)
        device.letter(3, symbol03)
        time.sleep(2)

        device.clear()

        #ASCII codes 
        symbol01 = 36
        symbol02 = 218
        symbol03 = 45
        symbol04 = 32
        
  
        #music
        device.clear()
        device.letter(0, symbol01)
        time.sleep(1)
        device.letter(1, symbol01)
        time.sleep(1)
        device.letter(2, symbol01)
        time.sleep(1)
        device.letter(3, symbol01)
        time.sleep(2)
        device.clear(0)
        time.sleep(1)
        device.clear(1)
        time.sleep(1)
        device.clear(2)
        time.sleep(1)
        device.clear(3)
        
        time.sleep(2)

        device.show_message("*** HARDCORE LAHRHOF ***")

        time.sleep(2)

        
      
except KeyboardInterrupt:
    device.clear()
  
    
    
    






