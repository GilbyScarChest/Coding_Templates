#### Percentage Calculator ####
#### By Tyler Gilbert ####

sm = 5    # small number OR percent(if under 100)
lg = 20   # large number


def percent_diff(sm_num, lg_num):
	'''gives you the percent difference of two numbers'''
	number = (lg_num - sm_num) / lg_num * 100
	return str(round(number, 2)) + "%"



def percent_of(sm_num, lg_num):
	'''gives you what percent the small number is of the large number'''
	number = (sm_num / lg_num) * 100
	return str(round(number, 2)) + "%"



def what_percent(perc, num):
	'''gives you what percent one number is to another'''
	percent = (perc / 100) * num
	return round(percent, 2)



print('')
print(f"The % difference between {sm} and {lg} is: _{percent_diff(sm, lg)}_")
print("##################################################")
print('')
print(f"{sm} is _{percent_of(sm, lg)}_ of {lg}")
print("##################################################")
print('')
print(f"{sm}% of {lg} is: _{what_percent(sm, lg)}_")
print("##################################################")
