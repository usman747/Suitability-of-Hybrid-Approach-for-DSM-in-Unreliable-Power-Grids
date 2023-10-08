import pandas as pd 
import math
import numpy as np

battery_size = 20
blackout_case = 1
soc_at_start = 70
priority_value = 5
charging_rate = 10
random_run_level = 0
random_run_capacity_value = 0 
random_run_expensive_level = 0
random_run_expensive_capacity_value = 0


soc_at1, soc_at2, soc_at3, soc_at4, soc_at5, soc_at6, soc_at7, soc_at8 = 0,0,0,0,0,0,0,0
soc_at9, soc_at10, soc_at11, soc_at12, soc_at13, soc_at14, soc_at15, soc_at16 = 0,0,0,0,0,0,0,0
soc_at17, soc_at18, soc_at19, soc_at20, soc_at21, soc_at22, soc_at23, soc_at24 = 0,0,0,0,0,0,0,0


df = pd.read_excel('TotalLoadperHour.xlsx')


column = df['PowerUsage']
column.index = np.arange(1,len(column)+1)


#Calculating SOC decrement per hour for each hour according to load profile 
soc_decrement_per_hour = (column / battery_size)* 100
# soc_decrement_per_hour = round(soc_decrement_per_hour,2)
#print(soc_decrement_per_hour)



#----------------------------------------------------Case_1---------------------------------------------#


def socUpdate_case1():

    global soc_at1, soc_at2, soc_at3, soc_at4, soc_at5, soc_at6, soc_at7, soc_at8
    global soc_at9, soc_at10, soc_at11, soc_at12, soc_at13, soc_at14, soc_at15, soc_at16
    global soc_at17, soc_at18, soc_at19, soc_at20, soc_at21, soc_at22, soc_at23, soc_at24
    soc_at1 = soc_at_start
    soc_at2 = soc_at_start
    soc_at3 = soc_at_start
    soc_at4 = soc_at_start
    soc_at5 = soc_at_start - soc_decrement_per_hour[4] # scheduled power outage
    soc_at6 = soc_at5
    soc_at7 = soc_at5
    soc_at8 = soc_at5
    soc_at9 = soc_at5
    soc_at10 = soc_at9 - soc_decrement_per_hour[9] # scheduled power outage
    soc_at11 = soc_at10
    soc_at12 = soc_at10
    soc_at13 = soc_at10
    soc_at14 = soc_at10
    soc_at15 = soc_at10
    soc_at16 = soc_at15 - soc_decrement_per_hour[15] # scheduled power outage
    soc_at17 = soc_at16
    soc_at18 = soc_at16
    soc_at19 = soc_at18 - soc_decrement_per_hour[18] # peak hour, DSM mode ON
    soc_at20 = soc_at19 - soc_decrement_per_hour[19] # peak hour, DSM mode ON
    soc_at21 = soc_at20 - soc_decrement_per_hour[20] # peak hour, DSM mode ON
    soc_at22 = soc_at21 - soc_decrement_per_hour[21] # peak hour, DSM mode ON
    soc_at23 = soc_at22 - soc_decrement_per_hour[22] # peak hour, DSM mode ON
    soc_at24 = soc_at23


#----------------------------------------------------Case_2---------------------------------------------#

def socUpdate_case2():

    global soc_at1, soc_at2, soc_at3, soc_at4, soc_at5, soc_at6, soc_at7, soc_at8
    global soc_at9, soc_at10, soc_at11, soc_at12, soc_at13, soc_at14, soc_at15, soc_at16
    global soc_at17, soc_at18, soc_at19, soc_at20, soc_at21, soc_at22, soc_at23, soc_at24
    soc_at1 = soc_at_start
    soc_at2 = soc_at_start
    soc_at3 = soc_at_start
    soc_at4 = soc_at_start
    soc_at5 = soc_at_start - soc_decrement_per_hour[4] # scheduled power outage
    soc_at6 = soc_at5
    soc_at7 = soc_at5
    soc_at8 = soc_at5
    soc_at9 = soc_at5
    soc_at10 = soc_at9 - soc_decrement_per_hour[9] # scheduled power outage
    soc_at11 = soc_at10
    soc_at12 = soc_at10
    soc_at13 = soc_at10
    soc_at14 = soc_at13 - soc_decrement_per_hour[13] # random power outage at 13 predicted by ML model
    soc_at15 = soc_at14 
    soc_at16 = soc_at15 - soc_decrement_per_hour[15] # scheduled power outage
    soc_at17 = soc_at16
    soc_at18 = soc_at16
    soc_at19 = soc_at18 - soc_decrement_per_hour[18] # peak hour, DSM mode ON
    soc_at20 = soc_at19 - soc_decrement_per_hour[19] # peak hour, DSM mode ON
    soc_at21 = soc_at20 - soc_decrement_per_hour[20] # peak hour, DSM mode ON
    soc_at22 = soc_at21 - soc_decrement_per_hour[21] # peak hour, DSM mode ON
    soc_at23 = soc_at22 - soc_decrement_per_hour[22] # peak hour, DSM mode ON
    soc_at24 = soc_at23


#----------------------------------------------------Case_3---------------------------------------------#

def socUpdate_case3():

    global soc_at1, soc_at2, soc_at3, soc_at4, soc_at5, soc_at6, soc_at7, soc_at8
    global soc_at9, soc_at10, soc_at11, soc_at12, soc_at13, soc_at14, soc_at15, soc_at16
    global soc_at17, soc_at18, soc_at19, soc_at20, soc_at21, soc_at22, soc_at23, soc_at24
    soc_at1 = soc_at_start
    soc_at2 = soc_at_start
    soc_at3 = soc_at_start
    soc_at4 = soc_at_start
    soc_at5 = soc_at_start - soc_decrement_per_hour[4] # scheduled power outage
    soc_at6 = soc_at5
    soc_at7 = soc_at5
    soc_at8 = soc_at5
    soc_at9 = soc_at5
    soc_at10 = soc_at9 - soc_decrement_per_hour[9] # scheduled power outage
    soc_at11 = soc_at10
    soc_at12 = soc_at10
    soc_at13 = soc_at10
    soc_at14 = soc_at13 - soc_decrement_per_hour[13] # random power outage at 13 predicted by ML model
    soc_at15 = soc_at14 
    soc_at16 = soc_at15 - soc_decrement_per_hour[15] # scheduled power outage
    soc_at17 = soc_at16
    soc_at18 = soc_at16
    soc_at19 = soc_at18 - soc_decrement_per_hour[18] # peak hour, DSM mode ON
    soc_at20 = soc_at19 - soc_decrement_per_hour[19] # peak hour, DSM mode ON
    soc_at21 = soc_at20 - soc_decrement_per_hour[20] # peak hour, DSM mode ON
    soc_at22 = soc_at21 - soc_decrement_per_hour[21] # random power outage at 10 predicted by ML model
    soc_at23 = soc_at22 - soc_decrement_per_hour[22] # peak hour, DSM mode ON
    soc_at24 = soc_at23


#----------------------------------------------------Case_4---------------------------------------------#

def socUpdate_case4():

    global soc_at1, soc_at2, soc_at3, soc_at4, soc_at5, soc_at6, soc_at7, soc_at8
    global soc_at9, soc_at10, soc_at11, soc_at12, soc_at13, soc_at14, soc_at15, soc_at16
    global soc_at17, soc_at18, soc_at19, soc_at20, soc_at21, soc_at22, soc_at23, soc_at24
    soc_at1 = soc_at_start
    soc_at2 = soc_at_start
    soc_at3 = soc_at_start
    soc_at4 = soc_at_start
    soc_at5 = soc_at_start - soc_decrement_per_hour[4] # scheduled power outage
    soc_at6 = soc_at5
    soc_at7 = soc_at5
    soc_at8 = soc_at5
    soc_at9 = soc_at5
    soc_at10 = soc_at9 - soc_decrement_per_hour[9] # scheduled power outage
    soc_at11 = soc_at10
    soc_at12 = soc_at10
    soc_at13 = soc_at10
    soc_at14 = soc_at13 - soc_decrement_per_hour[13] # random power outage at 13 predicted by ML model
    soc_at15 = soc_at14 
    soc_at16 = soc_at15 - soc_decrement_per_hour[15] # scheduled power outage
    soc_at17 = soc_at16
    soc_at18 = soc_at16
    soc_at19 = soc_at18 - soc_decrement_per_hour[18] # peak hour, DSM mode ON
    soc_at20 = soc_at19 - soc_decrement_per_hour[19] # peak hour, DSM mode ON
    soc_at21 = soc_at20 - soc_decrement_per_hour[20] # peak hour, DSM mode ON
    soc_at22 = soc_at21 - soc_decrement_per_hour[21] # random power outage at 22 predicted by ML model
    soc_at23 = soc_at22 - soc_decrement_per_hour[22] # peak hour, DSM mode ON
    soc_at24 = soc_at23 - soc_decrement_per_hour[23] # random power outage at 23 predicted by ML model




predictor_column = df['RandomPrediction']
predictor_column.index = np.arange(1,len(column)+1)
print(predictor_column)

predictor_column_counts = predictor_column.value_counts()
count_of_zeros = predictor_column_counts.get(0,0)
if count_of_zeros == 0:
    random_run_level = 1
    random_run_capacity_value = 0
    random_run_expensive_level = 1
    random_run_expensive_capacity_value = 0

if count_of_zeros == 1:
    random_run_level = 0
    random_run_capacity_value = 1
    random_run_expensive_level = 1
    random_run_expensive_capacity_value = 0

if count_of_zeros == 2:
    random_run_level = 1
    random_run_capacity_value = 2
    random_run_expensive_level = 1
    random_run_expensive_capacity_value = 1

if count_of_zeros == 3:
    random_run_level = 1
    random_run_capacity_value = 2
    random_run_expensive_level = 1
    random_run_expensive_capacity_value = 2

#print(count_of_zeros)



if random_run_capacity_value == 0:
    socUpdate_case1()

elif random_run_capacity_value == 1:
    socUpdate_case2()

elif random_run_capacity_value == 2:
    if random_run_expensive_capacity_value == 1:
        socUpdate_case3()
    else:
        socUpdate_case4()
        print("case4")








def write_pddl_problem_file(problem_name, init, goal):
    problem_file = open(problem_name + ".pddl", "w")
    problem_file.write("(define (problem " + problem_name + ")\n")
    problem_file.write("(:domain CompleteUnInterruptedPowerSupply)\n")
    problem_file.write("(:init\n")
    for fact in init:
        problem_file.write("  " + fact + "\n")
    problem_file.write(")\n")
    problem_file.write("(:goal\n")
    problem_file.write("  (and\n")
    for cond in goal:
        problem_file.write("    " + cond + "\n")
    problem_file.write("  )\n")
    problem_file.write(")\n")
    problem_file.write(")\n")
    problem_file.close()


#----------------------------------------------------Init_1--------------------------------------------#
problem_name = "CompleteUnInterruptedPowerSupplyProblem"
init = ["(begin)", 
        "(at 0.1 (not(begin)))", 
        "(charging_now)",
        "(=(lower_limit)40)", 
        "(=(upper_limit)100)",
        "(=(battery_soc)"+ str(soc_at_start) + ")",
        "(=(charging_rate)"+ str(charging_rate) + ")",
        "(=(cheap_priority_level)0)",
        "(=(priority_value)"+ str(priority_value) + ")",
        "(=(random_run_level)"+ str(random_run_level) + ")",
        "(=(random_run_capacity_value)"+ str(random_run_capacity_value) + ")",
        "(=(random_run_expensive_level)"+ str(random_run_expensive_level) + ")",
        "(=(random_run_expensive_capacity_value)"+ str(random_run_expensive_capacity_value) + ")",
        " ",
        "(at 0.1 (off_peak))",
        "(at 0.1 (is_not_blackout))",
        "(at 0.1 (is_not_random_blackout))", 
        "(at 1.0 (= (battery_soc)" + str(soc_at1) + "))", 
        "(at 2.0 (= (battery_soc)" + str(soc_at2) + "))", 
        "(at 3.0 (= (battery_soc)" + str(soc_at3) + "))", 
        "(at 4.0 (= (battery_soc)" + str(soc_at4) + "))", 
         " ",       
        "(at 4.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
        "(at 5.0 (is_not_blackout))",
        "(at 5.0 (= (battery_soc)" + str(soc_at5) + "))", 
        " ",
        "(at 6.0 (= (battery_soc) " + str(soc_at6) + "))", 
        "(at 7.0 (= (battery_soc) " + str(soc_at7) + "))", 
        "(at 8.0 (= (battery_soc) " + str(soc_at8) + "))", 
        "(at 9.0 (= (battery_soc) " + str(soc_at9) + "))", 
        " ",
        "(at 9.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE",
        "(at 10.0 (is_not_blackout))", 
        "(at 10.0 (= (battery_soc)" + str(soc_at10) + "))", 
        " ",
        "(at 11.0 (= (battery_soc) " + str(soc_at11) + "))", 
        "(at 12.0 (= (battery_soc) " + str(soc_at12) + "))", 
        "(at 13.0 (= (battery_soc) " + str(soc_at13) + "))",
        "(at 14.0 (= (battery_soc) " + str(soc_at14) + "))", 
        "(at 15.0 (= (battery_soc) " + str(soc_at15) + "))", 
        " ",
        "(at 15.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
        "(at 16.0 (is_not_blackout))", 
        "(at 16.0 (= (battery_soc) " + str(soc_at16) + "))", 
        " ",
        "(at 17.0 (= (battery_soc) " + str(soc_at17) + "))",
        "(at 18.0 (= (battery_soc) " + str(soc_at18) + "))", 
        " ",
        "(at 17.98 (not(off_peak)))",
        "(at 17.99 (peak))", 
        "(at 19.0 (= (battery_soc)" + str(soc_at19) + "))",
        "(at 20.0 (= (battery_soc)" + str(soc_at20) + "))",
        "(at 21.0 (= (battery_soc)" + str(soc_at21) + "))",
        "(at 22.0 (= (battery_soc)" + str(soc_at22) + "))",
        "(at 23.0 (= (battery_soc)" + str(soc_at23) + "))",
        "(at 23.01 (not(peak)))",
        "(at 23.02 (off_peak))",
        " ",
        "(at 24 (day_ended))"    ]

#----------------------------------------------------Init_2--------------------------------------------#
init_2 = ["(begin)", 
        "(at 0.1 (not(begin)))", 
        "(charging_now)",
        "(=(lower_limit)40)", 
        "(=(upper_limit)100)",
        "(=(battery_soc)"+ str(soc_at_start) + ")",
        "(=(charging_rate)"+ str(charging_rate) + ")",
        "(=(cheap_priority_level)0)",
        "(=(priority_value)"+ str(priority_value) + ")",
        "(=(random_run_level)"+ str(random_run_level) + ")",
        "(=(random_run_capacity_value)"+ str(random_run_capacity_value) + ")",
        "(=(random_run_expensive_level)"+ str(random_run_expensive_level) + ")",
        "(=(random_run_expensive_capacity_value)"+ str(random_run_expensive_capacity_value) + ")",
        " ",
        "(at 0.1 (off_peak))",
        "(at 0.1 (is_not_blackout))",
        "(at 0.1 (is_not_random_blackout))", 
        "(at 1.0 (= (battery_soc)" + str(soc_at1) + "))", 
        "(at 2.0 (= (battery_soc)" + str(soc_at2) + "))", 
        "(at 3.0 (= (battery_soc)" + str(soc_at3) + "))", 
        "(at 4.0 (= (battery_soc)" + str(soc_at4) + "))", 
         " ",       
        "(at 4.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
        "(at 5.0 (is_not_blackout))",
        "(at 5.0 (= (battery_soc)" + str(soc_at5) + "))", 
        " ",
        "(at 6.0 (= (battery_soc) " + str(soc_at6) + "))", 
        "(at 7.0 (= (battery_soc) " + str(soc_at7) + "))", 
        "(at 8.0 (= (battery_soc) " + str(soc_at8) + "))", 
        "(at 9.0 (= (battery_soc) " + str(soc_at9) + "))", 
        " ",
        "(at 9.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE",
        "(at 10.0 (is_not_blackout))", 
        "(at 10.0 (= (battery_soc)" + str(soc_at10) + "))", 
        " ",
        "(at 11.0 (= (battery_soc) " + str(soc_at11) + "))", 
        "(at 12.0 (= (battery_soc) " + str(soc_at12) + "))", 
        "(at 13.0 (= (battery_soc) " + str(soc_at13) + "))",
        " ",
        "(at 13.0 (not(is_not_random_blackout))) ; RANDOM POWER OUTAGE",
        "(at 14.0 (is_not_random_blackout))", 
        "(at 14.0 (= (battery_soc) " + str(soc_at14) + "))", 
        " ",
        "(at 15.0 (= (battery_soc) " + str(soc_at15) + "))", 
        " ",
        "(at 15.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
        "(at 16.0 (is_not_blackout))", 
        "(at 16.0 (= (battery_soc) " + str(soc_at16) + "))", 
        " ",
        "(at 17.0 (= (battery_soc) " + str(soc_at17) + "))",
        "(at 18.0 (= (battery_soc) " + str(soc_at18) + "))", 
        " ",
        "(at 17.98 (not(off_peak)))",
        "(at 17.99 (peak))", 
        "(at 19.0 (= (battery_soc)" + str(soc_at19) + "))",
        "(at 20.0 (= (battery_soc)" + str(soc_at20) + "))",
        "(at 21.0 (= (battery_soc)" + str(soc_at21) + "))",
        "(at 22.0 (= (battery_soc)" + str(soc_at22) + "))",
        "(at 23.0 (= (battery_soc)" + str(soc_at23) + "))",
        "(at 23.01 (not(peak)))",
        "(at 23.02 (off_peak))",
        " ",
        "(at 24 (day_ended))"    ]


#----------------------------------------------------Init_2b--------------------------------------------#
# init_2b = ["(begin)", 
#         "(at 0.1 (not(begin)))", 
#         "(charging_now)",
#         "(=(lower_limit)40)", 
#         "(=(upper_limit)100)",
#         "(=(battery_soc)"+ str(soc_at_start) + ")",
#         "(=(charging_rate)"+ str(charging_rate) + ")",
#         "(=(cheap_priority_level)0)",
#         "(=(priority_value)"+ str(priority_value) + ")",
#         "(=(random_run_level)"+ str(random_run_level) + ")",
#         "(=(random_run_capacity_value)"+ str(random_run_capacity_value) + ")",
#         "(=(random_run_expensive_level)"+ str(random_run_expensive_level) + ")",
#         "(=(random_run_expensive_capacity_value)"+ str(random_run_expensive_capacity_value) + ")",
#         " ",
#         "(at 0.1 (off_peak))",
#         "(at 0.1 (is_not_blackout))",
#         "(at 0.1 (is_not_random_blackout))", 
#         "(at 1.0 (= (battery_soc)" + str(soc_at1) + "))", 
#         "(at 2.0 (= (battery_soc)" + str(soc_at2) + "))", 
#         "(at 3.0 (= (battery_soc)" + str(soc_at3) + "))", 
#         "(at 4.0 (= (battery_soc)" + str(soc_at4) + "))", 
#          " ",       
#         "(at 4.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
#         "(at 5.0 (is_not_blackout))",
#         "(at 5.0 (= (battery_soc)" + str(soc_at5) + "))", 
#         " ",
#         "(at 6.0 (= (battery_soc) " + str(soc_at6) + "))", 
#         "(at 7.0 (= (battery_soc) " + str(soc_at7) + "))", 
#         "(at 8.0 (= (battery_soc) " + str(soc_at8) + "))", 
#         "(at 9.0 (= (battery_soc) " + str(soc_at9) + "))", 
#         " ",
#         "(at 9.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE",
#         "(at 10.0 (is_not_blackout))", 
#         "(at 10.0 (= (battery_soc)" + str(soc_at10) + "))", 
#         " ",
#         "(at 11.0 (= (battery_soc) " + str(soc_at11) + "))", 
#         "(at 12.0 (= (battery_soc) " + str(soc_at12) + "))", 
#         "(at 13.0 (= (battery_soc) " + str(soc_at13) + "))",
#         " ",
#         "(at 13.0 (not(is_not_random_blackout))) ; RANDOM POWER OUTAGE",
#         "(at 14.0 (is_not_random_blackout))", 
#         "(at 14.0 (= (battery_soc) " + str(soc_at14) + "))", 
#         " ",
#         "(at 15.0 (= (battery_soc) " + str(soc_at15) + "))", 
#         " ",
#         "(at 15.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
#         "(at 16.0 (is_not_blackout))", 
#         "(at 16.0 (= (battery_soc) " + str(soc_at16) + "))", 
#         " ",
#         "(at 17.0 (= (battery_soc) " + str(soc_at17) + "))",
#         "(at 18.0 (= (battery_soc) " + str(soc_at18) + "))", 
#         " ",
#         "(at 17.98 (not(off_peak)))",
#         "(at 17.99 (peak))", 
#         "(at 19.0 (= (battery_soc)" + str(soc_at19) + "))",
#         "(at 20.0 (= (battery_soc)" + str(soc_at20) + "))",
#         "(at 21.0 (= (battery_soc)" + str(soc_at21) + "))",
#         " ",
#         "(at 21.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
#         "(at 22.0 (is_not_blackout))", 
#         " ",
#         "(at 22.0 (= (battery_soc)" + str(soc_at22) + "))",
#         "(at 23.0 (= (battery_soc)" + str(soc_at23) + "))",
#         "(at 23.01 (not(peak)))",
#         "(at 23.02 (off_peak))",
#         " ",
#         "(at 24 (day_ended))"    ]

#----------------------------------------------------Init_3--------------------------------------------#
init_3 = ["(begin)", 
        "(at 0.1 (not(begin)))", 
        "(charging_now)",
        "(=(lower_limit)40)", 
        "(=(upper_limit)100)",
        "(=(battery_soc)"+ str(soc_at_start) + ")",
        "(=(charging_rate)"+ str(charging_rate) + ")",
        "(=(cheap_priority_level)0)",
        "(=(priority_value)"+ str(priority_value) + ")",
        "(=(random_run_level)"+ str(random_run_level) + ")",
        "(=(random_run_capacity_value)"+ str(random_run_capacity_value) + ")",
        "(=(random_run_expensive_level)"+ str(random_run_expensive_level) + ")",
        "(=(random_run_expensive_capacity_value)"+ str(random_run_expensive_capacity_value) + ")",
        " ",
        "(at 0.1 (off_peak))",
        "(at 0.1 (is_not_blackout))",
        "(at 0.1 (is_not_random_blackout))", 
        "(at 1.0 (= (battery_soc)" + str(soc_at1) + "))", 
        "(at 2.0 (= (battery_soc)" + str(soc_at2) + "))", 
        "(at 3.0 (= (battery_soc)" + str(soc_at3) + "))", 
        "(at 4.0 (= (battery_soc)" + str(soc_at4) + "))", 
         " ",       
        "(at 4.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
        "(at 5.0 (is_not_blackout))",
        "(at 5.0 (= (battery_soc)" + str(soc_at5) + "))", 
        " ",
        "(at 6.0 (= (battery_soc) " + str(soc_at6) + "))", 
        "(at 7.0 (= (battery_soc) " + str(soc_at7) + "))", 
        "(at 8.0 (= (battery_soc) " + str(soc_at8) + "))", 
        "(at 9.0 (= (battery_soc) " + str(soc_at9) + "))", 
        " ",
        "(at 9.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE",
        "(at 10.0 (is_not_blackout))", 
        "(at 10.0 (= (battery_soc)" + str(soc_at10) + "))", 
        " ",
        "(at 11.0 (= (battery_soc) " + str(soc_at11) + "))", 
        "(at 12.0 (= (battery_soc) " + str(soc_at12) + "))", 
        "(at 13.0 (= (battery_soc) " + str(soc_at13) + "))",
        " ",
        "(at 13.0 (not(is_not_random_blackout))) ; RANDOM POWER OUTAGE",
        "(at 14.0 (is_not_random_blackout))", 
        "(at 14.0 (= (battery_soc) " + str(soc_at14) + "))", 
        " ",
        "(at 15.0 (= (battery_soc) " + str(soc_at15) + "))", 
        " ",
        "(at 15.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
        "(at 16.0 (is_not_blackout))", 
        "(at 16.0 (= (battery_soc) " + str(soc_at16) + "))", 
        " ",
        "(at 17.0 (= (battery_soc) " + str(soc_at17) + "))",
        "(at 18.0 (= (battery_soc) " + str(soc_at18) + "))", 
        " ",
        "(at 17.98 (not(off_peak)))",
        "(at 17.99 (peak))", 
        "(at 19.0 (= (battery_soc)" + str(soc_at19) + "))",
        "(at 20.0 (= (battery_soc)" + str(soc_at20) + "))",
        "(at 21.0 (= (battery_soc)" + str(soc_at21) + "))",
        " ",      
        "(at 21.0 (random_shed_during_peak)) ; RANDOM POWER OUTAGE COMING AHEAD" ,
        "(at 22.0 (= (battery_soc)" + str(soc_at22) + "))",
        "(at 22.0 (not(is_not_random_blackout))) ; RANDOM POWER OUTAGE",
        "(at 23.0 (is_not_random_blackout))", 
        " ",
        "(at 23.0 (= (battery_soc)" + str(soc_at23) + "))",
        "(at 23.01 (not(peak)))",
        "(at 23.02 (off_peak))",
        " ",
        "(at 24 (day_ended))"    ]


#----------------------------------------------------Init_4--------------------------------------------#
init_4 = ["(begin)", 
        "(at 0.1 (not(begin)))", 
        "(charging_now)",
        "(=(lower_limit)40)", 
        "(=(upper_limit)100)",
        "(=(battery_soc)"+ str(soc_at_start) + ")",
        "(=(charging_rate)"+ str(charging_rate) + ")",
        "(=(cheap_priority_level)0)",
        "(=(priority_value)"+ str(priority_value) + ")",
        "(=(random_run_level)"+ str(random_run_level) + ")",
        "(=(random_run_capacity_value)"+ str(random_run_capacity_value) + ")",
        "(=(random_run_expensive_level)"+ str(random_run_expensive_level) + ")",
        "(=(random_run_expensive_capacity_value)"+ str(random_run_expensive_capacity_value) + ")",
        " ",
        "(at 0.1 (off_peak))",
        "(at 0.1 (is_not_blackout))",
        "(at 0.1 (is_not_random_blackout))", 
        "(at 1.0 (= (battery_soc)" + str(soc_at1) + "))", 
        "(at 2.0 (= (battery_soc)" + str(soc_at2) + "))", 
        "(at 3.0 (= (battery_soc)" + str(soc_at3) + "))", 
        "(at 4.0 (= (battery_soc)" + str(soc_at4) + "))", 
         " ",       
        "(at 4.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
        "(at 5.0 (is_not_blackout))",
        "(at 5.0 (= (battery_soc)" + str(soc_at5) + "))", 
        " ",
        "(at 6.0 (= (battery_soc) " + str(soc_at6) + "))", 
        "(at 7.0 (= (battery_soc) " + str(soc_at7) + "))", 
        "(at 8.0 (= (battery_soc) " + str(soc_at8) + "))", 
        "(at 9.0 (= (battery_soc) " + str(soc_at9) + "))", 
        " ",
        "(at 9.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE",
        "(at 10.0 (is_not_blackout))", 
        "(at 10.0 (= (battery_soc)" + str(soc_at10) + "))", 
        " ",
        "(at 11.0 (= (battery_soc) " + str(soc_at11) + "))", 
        "(at 12.0 (= (battery_soc) " + str(soc_at12) + "))", 
        "(at 13.0 (= (battery_soc) " + str(soc_at13) + "))",
        " ",
        "(at 13.0 (not(is_not_random_blackout))) ; RANDOM POWER OUTAGE",
        "(at 14.0 (is_not_random_blackout))", 
        "(at 14.0 (= (battery_soc) " + str(soc_at14) + "))", 
        " ",
        "(at 15.0 (= (battery_soc) " + str(soc_at15) + "))", 
        " ",
        "(at 15.0 (not(is_not_blackout))) ;SCHEDULED POWER OUTAGE", 
        "(at 16.0 (is_not_blackout))", 
        "(at 16.0 (= (battery_soc) " + str(soc_at16) + "))", 
        " ",
        "(at 17.0 (= (battery_soc) " + str(soc_at17) + "))",
        "(at 18.0 (= (battery_soc) " + str(soc_at18) + "))", 
        " ",
        "(at 17.98 (not(off_peak)))",
        "(at 17.99 (peak))", 
        "(at 19.0 (= (battery_soc)" + str(soc_at19) + "))",
        "(at 20.0 (= (battery_soc)" + str(soc_at20) + "))",
        "(at 21.0 (= (battery_soc)" + str(soc_at21) + "))",
        " ",      
        "(at 21.0 (random_shed_during_peak)) ; RANDOM POWER OUTAGE COMING AHEAD" ,
        "(at 22.0 (= (battery_soc)" + str(soc_at22) + "))",
        "(at 22.0 (not(is_not_random_blackout))) ; RANDOM POWER OUTAGE",
        "(at 23.0 (is_not_random_blackout))", 
        " ",
        "(at 23.0 (= (battery_soc)" + str(soc_at23) + "))",
        "(at 23.01 (not(peak)))",
        "(at 23.02 (off_peak))",
        " ",
        "(at 23.3 (not(is_not_random_blackout))) ; RANDOM POWER OUTAGE",
        "(at 24.0 (is_not_random_blackout))", 
        "(at 24.0 (= (battery_soc)" + str(soc_at24) + "))",
        " ",
        "(at 24 (day_ended))"    ]        


goal = ["(complete)"]

#--------------------------------------Writing Problem File---------------------------------------#

if random_run_capacity_value == 0:
    write_pddl_problem_file(problem_name, init, goal)

elif random_run_capacity_value == 1:
    write_pddl_problem_file(problem_name, init_2, goal)
    #write_pddl_problem_file(problem_name, init_2b, goal)

elif random_run_capacity_value == 2:
    if random_run_expensive_capacity_value == 1:
        write_pddl_problem_file(problem_name, init_3, goal)
    else:
        write_pddl_problem_file(problem_name, init_4, goal)
        print("case4")




