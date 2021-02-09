

file_orig = open("payments_orig.TXT", encoding='utf-8', mode="r")
file_result = open("payments_result.TXT", "w")
my_paym = file_orig.read()

if_ios = my_paym.split("\n")
if_ios_2 = []

for i in if_ios:

    if i.isdigit():
        if_ios_2.append("GPA." + i)
    else:
        if_ios_2.append(i)

my_paym = '\n'.join(if_ios_2)

lines = [x.split('\n') for x in my_paym.split("GPA")]

keys = ['order_id', 'date', 'sku', 'credited_at', 'content', 'what']

dicks = []

k = 1

for i in lines:
    if k >= len(lines):
        break
    cola = dict(zip(keys, lines[k]))
    dicks.append(cola)
    k = k + 1


def wild_dicks():
    value = i['sku'][:i['sku'].find('.')].split('_')
    price = str(int(value[3]) + 1)[:-2]
    return price


def trigger_dicks():
    value = i['sku'][:i['sku'].find('.')].split('_')
    return value


def check_special_dicks():
    result = ''
    kaila = ['special_offer', 'trigger_offer_fr', 'trigger_mech', 'trigger_offer_d_', 'trigger_offer_smallest', 'trigger_spectre', 'trigger_behemoth', 'trigger_fury_3zeus', 'trigger_hades', "trigger_strider", "trigger_raven", "trigger_tyr", 'trigger_falcon', 'trigger_griffin_2ion_2arbalest', 'trigger_leo_zeus_3gekko', 'trigger_blitz', 'trigger_rajin_2zeus', 'trigger_ao_guang', 'trigger_mender', 'trigger_stalker_3magnum', 'trigger_natasha_2zenit_2noricum', 'trigger_ao_jun', 'trigger_rogatka_2orkan', 'trigger_boa_thunder_orkan', 'trigger_mender', 'trigger_gareth_magnum_taran', 'trigger_patton_4gekko', 'trigger_hover_2storm_gust', 'trigger_keys_s_1', 'trigger_videoad_skip_premium', 'trigger_fury_3zeus', 'trigger_vityaz_trebuchet_2gekko']
    for item in kaila:
        if i['sku'].find(item) != -1:
            result = 'yes'
        else:
            continue
        return result


def find_sku_code():
    sku_code = ''
    marina = check_special_dicks()
    if marina == 'yes':
        sku_code = 'Special offer'
    # if i['sku'].find("special_offer") != -1 or i['sku'].find("trigger_offer_fr") != -1 or i['sku'].find("trigger_mech") != -1 or i['sku'].find("trigger_offer_d_") != -1 or i['sku'].find("trigger_offer_smallest") != -1 or i['sku'].find("trigger_spectre") != -1 or i['sku'].find("trigger_behemoth") != -1 or i['sku'].find("trigger_strider") != -1 or i['sku'].find("trigger_raven") != -1:
    #     sku_code = "Special offer"
    # elif i['sku'].find("trigger_strider") != -1 or i['sku'].find("trigger_raven") != -1 or i['sku'].find("trigger_tyr") != -1 or i['sku'].find("trigger_falcon") != -1 or i['sku'].find("trigger_griffin_2ion_2arbalest") != -1 or i['sku'].find("trigger_leo_zeus_3gekko") != -1:
    #     sku_code = "Special offer"
    # elif i['sku'].find("trigger_blitz") != -1 or i['sku'].find("trigger_rajin_2zeus") != -1 or i['sku'].find("trigger_ao_guang") != -1 or i['sku'].find("trigger_mender") != -1 or i['sku'].find("trigger_stalker_3magnum") != -1 or i['sku'].find("trigger_natasha_2zenit_2noricum") != -1:
    #     sku_code = "Special offer"
    # elif i['sku'].find("trigger_ao_jun") != -1 or i['sku'].find("trigger_rogatka_2orkan") != -1 or i['sku'].find("trigger_boa_thunder_orkan") != -1 or i['sku'].find("trigger_mender") != -1 or i['sku'].find("trigger_gareth_magnum_taran") != -1 or i['sku'].find("trigger_patton_4gekko") != -1:
    #     sku_code = "Special offer"
    # elif i['sku'].find("trigger_hover_2storm_gust") != -1 or i['sku'].find("trigger_keys_s_1") != -1 or i['sku'].find("trigger_videoad_skip_premium") != -1 or i['sku'].find("trigger_fury_3zeus") != -1 or i['sku'].find("trigger_vityaz_trebuchet_2gekko") != -1 or i['sku'].find("") != -1:
    #     sku_code = "Special offer"
    elif i['sku'].find("operation_pass") != -1:
        sku_code = "Operation pass"
    elif i['sku'].find("shards_trigger_offer") != -1:
        values = trigger_dicks()
        sku_code = f"Offer {values[3].capitalize()} {values[4]}"
    elif i['sku'].find("premium.") != -1:
        sku_code = i['sku'][9:10] + "days of Premium"
    elif i['sku'].find("starter_pack") != -1:
        sku_code = "Starter pack"
    elif i['sku'].find("wild_offer_for") != -1:
        n = wild_dicks()
        sku_code = f'Offer price {n}'
    elif i['sku'].find("gold_500_for_499") != -1:
        sku_code = "Gold bar"
    elif i['sku'].find("gold_1200_for_999") != -1:
        sku_code = "A few gold bars"
    elif i['sku'].find("gold_2500_for_1999") != -1:
        sku_code = "Small stash of gold bars"
    elif i['sku'].find("gold_6500_for_4999") != -1:
        sku_code = "Medium stash of gold bars"
    elif i['sku'].find("gold_14000_for_9999") != -1:
        sku_code = "Large stash of gold bars"
    elif i['sku'].find("platinum_big") != -1:
        sku_code = "Platinum Big"
    elif i['sku'].find("platinum_medium") != -1:
        sku_code = "Platinum Medium"
    elif i['sku'].find("platinum_small") != -1:
        sku_code = "Platinum Small"
    elif i['sku'].find("wr_coins_big") != -1:
        sku_code = "Big box of coins"
    elif i['sku'].find("wr_coins_medium") != -1:
        sku_code = "Medium box of coins"
    elif i['sku'].find("wr_coins_small") != -1:
        sku_code = "Small box of coins"
    elif i['sku'].find("trigger_offer_4_gekko_for_1999") != -1:
        sku_code = "Offer 4 Gekko"
    elif i['sku'].find("trigger_offer_4_trebuchet_for_3999") != -1:
        sku_code = "Offer 4 Trebuchet"
    elif i['sku'].find("trigger_offer_zeus_for_699") != -1:
        sku_code = "Offer Zeus"
    elif i['sku'].find("trigger_offer_taran_for_499") != -1:
        sku_code = "Offer Taran"
    elif i['sku'].find("trigger_offer_leo_for_499") != -1:
        sku_code = "Offer Leo"
    elif i['sku'].find("trigger_offer_2_trebuchet_2_trident_for_3999") != -1:
        sku_code = " Offer 2 Trebuchet + 2 Trident"
    elif i['sku'].find("trigger_offer_butch_for_7499") != -1:
        sku_code = "Offer Butch"
    elif i['sku'].find("trigger_offer_leo_3_magnum_for_2499") != -1:
        sku_code = " Offer Leo + 3 Magnum"
    elif i['sku'].find("trigger_offer_griffin_2_taran_for_1999") != -1:
        sku_code = " Offer Griffin + 2 Taran"
    elif i['sku'].find("trigger_offer_2_orkan_2_taran_for_2999") != -1:
        sku_code = " Offer 2 Orkan + 2 Taran"
    elif i['sku'].find("trigger_offer_2_orkan_for_1499") != -1:
        sku_code = "Offer 2 Orkan"
    elif i['sku'].find("trigger_offer_gareth_pinata_orkan_for_1499") != -1:
        sku_code = "Offer Gareth + Pinata + Orkan"
    elif i['sku'].find("trigger_offer_thunder_2_taran_for_1499") != -1:
        sku_code = " Offer Thunder + 2 Taran"
    elif i['sku'].find("trigger_offer_gareth_pin_tulumbas_for_699") != -1:
        sku_code = " Offer Gareth + Pin + Tulumbas"
    elif i['sku'].find("trigger_offer_thunder_2_orkan_for_1499") != -1:
        sku_code = " Offer Thunder + 2 Orkan"
    elif i['sku'].find("trigger_offer_kangdae_for_199") != -1:
        sku_code = "Offer Kang Dae"
    elif i['sku'].find("trigger_offer_3_trebuchet_for_2999") != -1:
        sku_code = "Offer 3 Trebuchet"
    elif i['sku'].find("trigger_offer_orkan_pinata_for_699") != -1:
        sku_code = "Offer Orkan + Pinata"
    elif i['sku'].find("trigger_offer_2_pinata_orkan_for_799") != -1:
        sku_code = "Offer 2 Pinata + Orkan"
    elif i['sku'].find("trigger_offer_4_trident_for_3999") != -1:
        sku_code = "Offer 4 Trident"
    elif i['sku'].find("trigger_offer_orkan_for_699") != -1:
        sku_code = "Offer Orkan"
    elif i['sku'].find("trigger_offer_golem_for_199") != -1:
        sku_code = "Offer Golem"
    elif i['sku'].find("trigger_offer_fujin_for_1499") != -1:
        sku_code = "Offer Fujin"
    elif i['sku'].find("trigger_offer_3_zeus_for_2499") != -1:
        sku_code = "Offer 3 Zeus"
    elif i['sku'].find("trigger_offer_patton_4_aphid_for_1999") != -1:
        sku_code = "Offer Patton + 4 Aphid"
    elif i['sku'].find("trigger_offer_4_aphid_for_1999") != -1:
        sku_code = "Offer 4 Aphid"
    elif i['sku'].find("trigger_offer_thunder_for_299") != -1:
        sku_code = "Offer Thunder"
    elif i['sku'].find("trigger_offer_2_trebuchet_for_1999") != -1:
        sku_code = "Offer 2 Trebuchet"
    elif i['sku'].find("trigger_offer_2_taran_for_1499") != -1:
        sku_code = "Offer 2 Taran"
    elif i['sku'].find("trigger_offer_stalker_for_999") != -1:
        sku_code = "Offer Stalker"
    elif i['sku'].find("trigger_offer_2_magnum_2_taran_for_2999") != -1:
        sku_code = "Offer 2 Magnum + 2 Taran"
    elif i['sku'].find("trigger_offer_3_taran_for_1999") != -1:
        sku_code = "Offer 3 Taran"
    elif i['sku'].find("trigger_offer_3_trident_for_3499") != -1:
        sku_code = "Offer 3 Trident"
    elif i['sku'].find("trigger_offer_trebuchet_for_999") != -1:
        sku_code = "Offer Trebuchet"
    elif i['sku'].find("trigger_offer_gepard_3_magnum_for_2499") != -1:
        sku_code = "Offer Gepard + 3 Magnum"
    elif i['sku'].find("trigger_offer_3_aphid_for_1499") != -1:
        sku_code = "Offer 3 Aphid"
    elif i['sku'].find("trigger_offer_2_trident_for_1999") != -1:
        sku_code = "Offer 2 Trident"
    elif i['sku'].find("trigger_offer_3_magnum_for_1499") != -1:
        sku_code = "Offer 3 Magnum"
    elif i['sku'].find("trigger_offer_3_orkan_for_1999") != -1:
        sku_code = "Offer 3 Orkan"
    elif i['sku'].find("trigger_offer_golem_2_gekko_for_999") != -1:
        sku_code = "Offer Golem + 2 Gekko"
    elif i['sku'].find("trigger_offer_rogatka_2_taran_for_2999") != -1:
        sku_code = "Offer Rogatka + 2 Taran"
    elif i['sku'].find("trigger_offer_orkan_magnum_for_1499") != -1:
        sku_code = "Offer Taran + Magnum"
    elif i['sku'].find("trigger_offer_4_magnum_for_1999") != -1:
        sku_code = "Offer 4 Magnum"
    elif i['sku'].find("trigger_offer_jesse_for_1999") != -1:
        sku_code = "Offer Jesse"
    elif i['sku'].find("trigger_offer_2_magnum_taran_for_1999") != -1:
        sku_code = "Offer 2 Magnum + Taran"
    elif i['sku'].find("trigger_offer_2_magnum_2_orkan_for_2999") != -1:
        sku_code = "Offer 2 Magnum + 2 Orkan"
    elif i['sku'].find("trigger_offer_raijin_2_zenit_for_2499") != -1:
        sku_code = "Offer Raijin + 2 Zenit"
    elif i['sku'].find("trigger_offer_2_zeus_for_1999") != -1:
        sku_code = "Offer Zeus"
    elif i['sku'].find("trigger_offer_griffin_natasha_leo_for_1499") != -1:
        sku_code = "Offer Griffin + Natasha + Leo"
    elif i['sku'].find("trigger_offer_raijin_for_1999") != -1:
        sku_code = "SOffer Raijin"
    elif i['sku'].find("trigger_offer_zenit_for_19") != -1:
        sku_code = "Offer Zenit"
    elif i['sku'].find("trigger_offer_2_magnum_orkan_for_1999") != -1:
        sku_code = "Offer 2 Magnum + Orkan"
    elif i['sku'].find("trigger_offer_gepard_3_aphid_for_1999") != -1:
        sku_code = "Offer Gepard + 3 Aphid"
    elif i['sku'].find("trigger_offer_magnum_taran_for_999") != -1:
        sku_code = "Offer Magnum + Taran"
    elif i['sku'].find("trigger_offer_2_gekko_for_999") != -1:
        sku_code = "Offer 2 Gekko"
    elif i['sku'].find("trigger_offer_rhino_for_1999") != -1:
        sku_code = "Offer Rhino"
    elif i['sku'].find("trigger_offer_rogatka_2_orkan_for_2999") != -1:
        sku_code = "Offer Rogatka + 2 Orkan"
    elif i['sku'].find("trigger_offer_2_magnum_for_999") != -1:
        sku_code = "Offer 2 Magnum"
    elif i['sku'].find("trigger_offer_4_orkan_for_2999") != -1:
        sku_code = "Offer 4 Orkan"
    elif i['sku'].find("trigger_offer_magnum_for_499") != -1:
        sku_code = "Offer Magnum"
    elif i['sku'].find("trigger_offer_2_orkan_2_pinata_for_1499") != -1:
        sku_code = "Offer 2 Orkan + 2 Pinata"
    elif i['sku'].find("Offer 2 Orkan + 2 Pinata") != -1:
        sku_code = "Small box of coins"
    elif i['sku'].find("wr_coins_small") != -1:
        sku_code = "Small box of coins"
    elif i['sku'].find("wr_coins_small") != -1:
        sku_code = "Small box of coins"
    elif i['sku'].find("wr_coins_small") != -1:
        sku_code = "Small box of coins"
    elif i['sku'].find("wr_coins_small") != -1:
        sku_code = "Small box of coins"
    elif i['sku'].find("wr_coins_small") != -1:
        sku_code = "Small box of coins"
    elif i['sku'].find("wr_coins_small") != -1:
        sku_code = "Small box of coins"

    return sku_code


for i in dicks:
    print(i['sku'])
    k = find_sku_code()
    print(f"GPA{i['order_id']} - {i['date'][3:13]} - {k}")
