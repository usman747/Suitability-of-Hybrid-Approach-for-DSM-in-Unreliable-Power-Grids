(define (problem CompleteUnInterruptedPowerSupplyProblem)
(:domain CompleteUnInterruptedPowerSupply)
(:init
  (begin)
  (at 0.1 (not(begin)))
  (charging_now)
  (=(lower_limit)40)
  (=(upper_limit)100)
  (=(battery_soc)70)
  (=(charging_rate)10)
  (=(cheap_priority_level)0)
  (=(priority_value)5)
  (=(random_run_level)1)
  (=(random_run_capacity_value)0)
  (=(random_run_expensive_level)1)
  (=(random_run_expensive_capacity_value)0)
   
  (at 0.1 (off_peak))
  (at 0.1 (is_not_blackout))
  (at 0.1 (is_not_random_blackout))
  (at 1.0 (= (battery_soc)70))
  (at 2.0 (= (battery_soc)70))
  (at 3.0 (= (battery_soc)70))
  (at 4.0 (= (battery_soc)70))
   
  (at 4.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE
  (at 5.0 (is_not_blackout))
  (at 5.0 (= (battery_soc)56.852175))
   
  (at 6.0 (= (battery_soc) 56.852175))
  (at 7.0 (= (battery_soc) 56.852175))
  (at 8.0 (= (battery_soc) 56.852175))
  (at 9.0 (= (battery_soc) 56.852175))
   
  (at 9.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE
  (at 10.0 (is_not_blackout))
  (at 10.0 (= (battery_soc)50.404333333333334))
   
  (at 11.0 (= (battery_soc) 50.404333333333334))
  (at 12.0 (= (battery_soc) 50.404333333333334))
  (at 13.0 (= (battery_soc) 50.404333333333334))
  (at 14.0 (= (battery_soc) 50.404333333333334))
  (at 15.0 (= (battery_soc) 50.404333333333334))
   
  (at 15.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE
  (at 16.0 (is_not_blackout))
  (at 16.0 (= (battery_soc) 45.82188333333333))
   
  (at 17.0 (= (battery_soc) 45.82188333333333))
  (at 18.0 (= (battery_soc) 45.82188333333333))
   
  (at 17.98 (not(off_peak)))
  (at 17.99 (peak))
  (at 19.0 (= (battery_soc)39.769425))
  (at 20.0 (= (battery_soc)29.294041666666665))
  (at 21.0 (= (battery_soc)10.500999999999994))
  (at 22.0 (= (battery_soc)-4.054641666666674))
  (at 23.0 (= (battery_soc)-14.886000000000008))
  (at 23.01 (not(peak)))
  (at 23.02 (off_peak))
   
  (at 24 (day_ended))
)
(:goal
  (and
    (complete)
  )
)
)
