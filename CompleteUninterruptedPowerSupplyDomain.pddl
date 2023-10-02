(define (domain CompleteUnInterruptedPowerSupply)
(:requirements
   :strips
   :fluents
   :numeric-fluents
   :durative-actions
   :timed-initial-literals
   :constraints
   :duration-inequalities

   :universal-preconditions
   :disjunctive-preconditions
   :conditional-effects
   :preferences
)

(:predicates(complete)(begin)
(enable) (day_ended) 
(is_decreasing)(is_increasing)
(peak) (off_peak) (blackout)
(is_not_blackout) (charging_now)
(is_not_random_blackout)
)



(:functions
(battery_soc)
(battery-soc-fix)
(lower_limit)(upper_limit)
(charging_rate)
(cheap_priority_level)
(priority_value)
(random_run_level)
(random_run_capacity_value)

)

(:durative-action Battery_Charge_Pre-Emptive_Cheaply
:parameters()
:duration (=?duration 0.33)
:condition(and 
         (at start(enable))
         (at start (charging_now))
         (over all (off_peak))
         (over all (is_not_blackout))
         (over all (is_not_random_blackout))
         (at start (<= (random_run_level) random_run_capacity_value))
         (at end (<= (+ (battery_soc) (battery-soc-fix)) (upper_limit)))
         ) 
:effect(and
(at end (increase (battery-soc-fix) charging_rate))
(at end (increase (random_run_level) 1))
(at end (increase (cheap_priority_level) 1))
(at start (not(charging_now)))
(at end (charging_now))
))

(:durative-action Battery_Charge_Pre-Emptive_Expensively
:parameters()
:duration (=?duration 0.33)
:condition(and 
         (at start(enable))
         (at start (charging_now))
         (over all (peak))
         (over all (is_not_blackout))
         (over all (is_not_random_blackout))
         (at start (>= (cheap_priority_level) priority_value))
         (at end (<= (+ (battery_soc) (battery-soc-fix)) (upper_limit)))
)
:effect(and
(at end (increase (battery-soc-fix) charging_rate))
(at end (is_increasing))
(at end (increase (random_run_level) 1))
(at start (not(charging_now)))
(at end (charging_now))
))










(:durative-action Battery_Charge_Cheaply
:parameters()
:duration (=?duration 0.33)
:condition(and 
         (at start(enable))
         (at start (charging_now))
         (over all (off_peak))
         (over all (is_not_blackout))
         (over all (is_not_random_blackout))
         (at start (>= (random_run_level) random_run_capacity_value))
         (at end (<= (+ (battery_soc) (battery-soc-fix)) (upper_limit)))
         ;the line above restricts it from charging over 100%,
         ) 
:effect(and
(at end (increase (battery-soc-fix) charging_rate))
(at end (increase (cheap_priority_level) 1))
(at end (increase (random_run_level) 1))
(at start (not(charging_now)))
(at end (charging_now))

))


(:durative-action Battery_Charge_Expensively
:parameters()
:duration (=?duration 0.33)
:condition(and 
         (at start(enable))
         (at start (charging_now))
         (over all (peak))
         (over all (is_not_blackout))
         (over all (is_not_random_blackout))
         (at start (>= (cheap_priority_level) priority_value))
         (at start (>= (random_run_level) random_run_capacity_value))
         (at end (<= (+ (battery_soc) (battery-soc-fix)) (upper_limit)))
)
:effect(and
(at end (increase (battery-soc-fix) charging_rate))
(at end (is_increasing))
(at start (not(charging_now)))
(at end (charging_now))
))




(:durative-action Day_Ahead_Plan 
:parameters()
:duration (<= ?duration 100)
:condition(and
   (at start(begin))
   (at end (day_ended))
   (over all (and   
   (<= (+ (battery_soc) (battery-soc-fix)) (upper_limit))
   (>= (+ (battery_soc) (battery-soc-fix)) (lower_limit))
   ))
)

:effect(and
(at start(enable))
(at end(complete)))
)








)
