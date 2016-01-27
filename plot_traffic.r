#Script to read in the data output from traffic_times.py and plot the average
#travel durations at each 10 minute interval across the three model types

traffic=read.csv('schaumburg_traffic.csv')

traffic$time = paste(traffic$hour,traffic$minute,sep='.')
traffic$time_nb = as.numeric(traffic$time)
traffic$time = factor(traffic$time)
traffic$new_day = ifelse(traffic$weekday==0,'Monday',
						ifelse(traffic$weekday==1,'Tuesday',
						ifelse(traffic$weekday==2,'Wednesday',
						ifelse(traffic$weekday==3,'Thursday',
						'Friday'))))
						
traffic$new_day=factor(traffic$new_day)
time_means = aggregate(duration~travel_type+model+time_nb,data=traffic,mean)
time_means$time_nb = as.numeric(time_means$time)

best_guess_t = time_means[time_means$model=="best_guess"&time_means$travel_type=="to_work",]
pessimistic_t = time_means[time_means$model=="pessimistic"&time_means$travel_type=="to_work",]
optimistic_t = time_means[time_means$model=="optimistic"&time_means$travel_type=="to_work",]

best_guess_f = time_means[time_means$model=="best_guess"&time_means$travel_type=="from_work",]
pessimistic_f = time_means[time_means$model=="pessimistic"&time_means$travel_type=="from_work",]
optimistic_f = time_means[time_means$model=="optimistic"&time_means$travel_type=="from_work",]

xrange_t = range(time_means$time_nb[time_means$travel_type=="to_work"])
yrange_t = range(time_means$duration[time_means$travel_type=="to_work"])

xrange_f = range(time_means$time_nb[time_means$travel_type=="from_work"])
yrange_f = range(time_means$duration[time_means$travel_type=="from_work"])

plot.new()
par(mfrow=c(1,2))

plot(xrange_t,yrange_t,type="n", xlab="Time(Hour:Minute)", ylab="Duration(Minutes)",lwd=1.5, col=1,xaxt="n") 
axis(1, at=time_means$time_nb[time_means$travel_type=="to_work"], las=2)
lines(pessimistic_t$time, pessimistic_t$duration, type="b", lwd=1.5, col=1) 
lines(best_guess_t$time, best_guess_t$duration, type="b", lwd=1.5, col=2)
lines(optimistic_t$time, optimistic_t$duration, type="b", lwd=1.5, col=3)
title("Travel Times To Schaumburg")

plot(xrange_f,yrange_f,type="n", xlab="Time(Hour:Minute)", ylab="Duration(Minutes)",lwd=1.5, col=1,xaxt="n") 
axis(1, at=time_means$time_nb[time_means$travel_type=="from_work"], las=2)
lines(pessimistic_f$time, pessimistic_f$duration, type="b", lwd=1.5, col=1) 
lines(best_guess_f$time, best_guess_f$duration, type="b", lwd=1.5, col=2)
lines(optimistic_f$time, optimistic_f$duration, type="b", lwd=1.5, col=3)

title("Travel Times From Schaumburg")
