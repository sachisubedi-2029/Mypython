valid_days = 0
high_temp = 0
freez_days = 0
hot_days = 0
heatwaves = 0
cold_spells = 0
low__temp = 5
hot = 0
cold = 0
while True:
    av_temeperature = int(input("Enter day's average temperature in celsius :"))
    day = int(input("Enter the days only upto 3 and restart from 1 after reaching 3 :"))
    if av_temeperature==999:
        break
    else:
        if av_temeperature<-50 and av_temeperature>60:
            print("Invalid tmperature!")
        elif day<=0:
            print("Invalid day")
        elif day>3:
            print("Invalid day")          
        else:
            if av_temeperature<=0:
                freez_days=freez_days+1
                valid_days=valid_days+1
                if av_temeperature>high_temp:
                    high_temp=av_temeperature
                if av_temeperature<low__temp:
                    low__temp=av_temeperature
            if av_temeperature>=35:
                hot_days=hot_days+1
                valid_days=valid_days
                if av_temeperature>high_temp:
                    high_temp=av_temeperature
                if av_temeperature<low__temp:
                    low__temp=av_temeperature     
        if day==1:
            if av_temeperature>=35:
                hot = hot+1
            if av_temeperature<=0:
                cold = cold+1    
        elif day==2:
            if av_temeperature>=35:
                hot = hot+1
            if av_temeperature<=0:
                cold = cold+1
        else:
            if av_temeperature>=35:
                hot = hot+1
            if av_temeperature<=0:    
                cold = cold+1                
            print("Heatwave detected") 
        if hot==3:
            heatwaves=heatwaves+1
            print("heatwave detected")
        if cold==3:
            cold_spells=cold_spells+1
            print("Cold spells detected")
if valid_days>0:
  print("Number of valid days =",valid_days)
  print("Highest temperature recorded =",high_temp)
  print("Lowest temperature recorded =",low__temp)
  print("Number of freezing days =",freez_days)
  print("Number of hot days =",hot_days)
  print("Number of heatwaves =",heatwaves)
  print("Number of cold spells =",cold_spells)
else:
    print("No valid days.So ,data isnot collected")  









                                    

                               



