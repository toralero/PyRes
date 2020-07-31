from operator import add, sub

tolerance = 2
max_tolerance = 10
bend = 10

budget = 1000000

ideals = {  'ch' : [3,6,2,4],
            'sw' : [2,1,7,5],
            'us' : [5,5,6,1]}

minmax = {  'ch' : [0, 1000],
            'sw' : [0, 60],
            'us' : [0, 2000]}

buyprice = {'ch' : 1000,
            'sw' : 2000,
            'us' : 900}

cheese_profiles = { 'm': [7,2,3,1],
                    'p': [4,5,8,4],
                    'r': [2,8,2,7],
                    'a': [4,1,3,4]}

cheese_cost = { 'm':6.7,
                'p':7.5,
                'r':8.6,
                'a':7.5}

def calculate_final_profile(mix_list):
    sum_profile = [0,0,0,0]
    for ch in mix_list:
        if ch == 'm':
            sum_profile = list(map(add, sum_profile, cheese_profiles['m']))
        elif ch == 'p':
            sum_profile = list(map(add, sum_profile, cheese_profiles['p']))     
        elif ch == 'r':
            sum_profile = list(map(add, sum_profile, cheese_profiles['r']))
        elif ch == 'a':
            sum_profile = list(map(add, sum_profile, cheese_profiles['a']))
        else:
            print("Unknown ingredient! You spoiled your mix!")
            sum_profile = list(map(add, sum_profile, [9999,9999,9999,9999]))
    return [round(s/len(mix_list)) for s in sum_profile]

def calculate_ideal_deviation(profile, ideal):
    deviation = 0
    for i in range(0, len(profile)):
        deviation += round(abs(ideal[i] - profile[i]))
    return deviation

def calculate_buy_volume(minmax, dev):
    diff = minmax[1] - minmax[0]
    
    if dev == 0:
        margin = diff
    elif dev <= max_tolerance:
        exp = -1 + (dev/max_tolerance) 
        margin = round(diff * (1-bend**exp))
    else:
        margin = 0

    return minmax[0] + margin

def price_of_mix(mix, cheese_cost):
    total_cost = 0
    for ch in mix:
        if ch == 'm':
            total_cost += cheese_cost['m']
        elif ch == 'p':
            total_cost += cheese_cost['p']
        elif ch == 'r':
            total_cost += cheese_cost['r']
        elif ch == 'a':
            total_cost += cheese_cost['a']
        else:
            print("You added a MAGICAL INGREDIENT")
            total_cost += 1000000000000
    
    return total_cost

def calculate_score(mix):
    if (isinstance(mix, list)):
        profile = calculate_final_profile(mix)
        
        ch_dev = calculate_ideal_deviation(profile, ideals['ch'])
        sw_dev = calculate_ideal_deviation(profile, ideals['sw'])
        us_dev = calculate_ideal_deviation(profile, ideals['us'])
        
        ch_vol = calculate_buy_volume(minmax['ch'], ch_dev)
        sw_vol = calculate_buy_volume(minmax['sw'], sw_dev)
        us_vol = calculate_buy_volume(minmax['us'], us_dev)

        price = price_of_mix(mix, cheese_cost)
        
        remaining = budget - price * (ch_vol + sw_vol + us_vol)
        if remaining < 0:
            rm_qty = abs(remaining)//price+1
            
            while rm_qty > 0:
                if(rm_qty >= us_vol):
                    rm_qty -= us_vol
                    us_vol = 0
                else:
                    us_vol -= rm_qty
                    rm_qty = 0

                if(rm_qty >= ch_vol):
                    rm_qty -= ch_vol
                    ch_vol = 0
                else:
                    ch_vol -= rm_qty
                    rm_qty = 0

                if(rm_qty >= sw_vol):
                    rm_qty -= sw_vol
                    sw_vol = 0
                else:
                    sw_vol -= rm_qty
                    rm_qty = 0


        score = ch_vol * buyprice['ch'] + sw_vol * buyprice['sw'] + us_vol * buyprice['us']
        score -= price * (ch_vol + sw_vol + us_vol)
        return score, price, {'ch':ch_vol, 'sw':sw_vol, 'us':us_vol}
    else:
        print("Please enter a list to this method.")
        return 0

def batch_calc(population):
    scores = []
    for i in range(0,len(population)):
        score,_,_ = calculate_score(population[i])
        scores.append(score)
    return scores
