file_orig = open("payments_orig.TXT", encoding='utf-8', mode="r")
file_result = open("payments_result.TXT", "w")
my_paym = file_orig.read()

if_ios = my_paym.split("\n")
if_ios_2 = []

for i in if_ios:

    if i.isdigit() or i.find('=:1:11') != -1:
        if_ios_2.append("GPA." + i)
    else:
        if_ios_2.append(i)

my_paym = '\n'.join(if_ios_2)

lines = [x.split('\n') for x in my_paym.split("GPA")]

keys = ['order_id', 'date', 'sku', 'credited_at', 'content', 'content0',
        'content1', 'content2', 'content3', 'content4', 'content5']

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
    kamilla = ['special_offer', 'trigger_offer_fr', 'trigger_mech', 'trigger_offer_d_',
               'trigger_offer_smallest', 'trigger_spectre', 'trigger_behemoth', 'trigger_fury_3zeus',
               'trigger_hades', "trigger_strider", "trigger_raven", "trigger_tyr",
               "trigger_falcon", "trigger_griffin_2ion_2arbalest", "trigger_leo_zeus_3gekko", "trigger_blitz",
               "trigger_rajin_2zeus", "trigger_ao_guang", "trigger_mender", "trigger_stalker_3magnum",
               "trigger_natasha_2zenit_2noricum", "trigger_ao_jun", "trigger_rogatka_2orkan",
               "trigger_boa_thunder_orkan", "trigger_mender", "trigger_gareth_magnum_taran", "trigger_patton_4gekko",
               "trigger_hover_2storm_gust", "trigger_keys_s_1", "trigger_videoad_skip_premium", "trigger_fury_3zeus",
               "trigger_vityaz_trebuchet_2gekko"]
    for item in kamilla:
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
    elif i['sku'].find("wr_coins_small") != -1:
        sku_code = "Small box of coins"
    elif i['sku'].find("wr_coins_small") != -1:
        sku_code = "Small box of coins"
    else:
        sku_code = 'Special Offer'

    return sku_code


def find_content():
    papirus = {'HARD': 'Au', 'SOFT': 'Ag', 'MODULE_CHARGE': 'Power cells', 'WR_COIN': 'coins',
               'PLATINUM': 'Platinum', 'Pass': 'Operation pass', 'GACHA_TOKEN': 'Keys'}

    papirus1 = {'ON_30HP_RESISTS': 'Recurrent Emergency Defender', 'ON_50HP_RESISTS': 'Recurrent Forewarning Defender',
                'ON_MODULEUSE_DAMAGE': 'Modulative Intensifier', 'AFTER_SUPPRESSION_DAMAGE': 'Resurgent Intensifier',
                'ON_SUPPRESSION_RESISTS': 'Impaired Defender', 'ON_ROOT_DAMAGE': 'Inhibited Intensifier',
                'ON_ROOT_RESISTS': 'Inhibited Defender', 'ON_ROOTCHARGE_RESISTS': 'Debilitating Defender',
                'ON_FREEZECHARGE_RESISTS': 'Arctic Defender', 'ON_BATTLEBORN_DAMAGE': 'Raging Intensifier',
                'ON_LASTSTAND_DAMAGE': 'Struggling Intensifier', 'ON_HEALMODULE_DAMAGE': 'Revitalizing Intensifier',
                'ON_HEALMODULE_RESISTS': 'Revitalizing Defender', 'ON_COOLDOWN_RESISTS': 'Recharging Defender',
                'ON_ROOTIMMUNE_DAMAGE': 'Unimpeded Intensifier', 'ON_SUPPRESSIONIMMUNE_DAMAGE': 'Inciting Intensifier',
                'ON_FREEZEIMMUNE_DAMAGE': 'Thermic Intensifier',
                'ON_HEAL_MOREHEAL_ABSOLUTE': 'Recurrent Reconstructive Repairer',
                'ON_HEAL_MOREHEAL_RELATIVE': 'Recurrent Reconstructive Renovator',
                'ON_SMALLDAMAGE_HEAL_ABSOLUTE': 'Recurrent In-trouble Repairer',
                'ON_SMALLDAMAGE_HEAL_RELATIVE': 'Recurrent In-trouble Renovator',
                'ON_LARGEDAMAGE_HEAL_ABSOLUTE': 'Recurrent Crashing Repairer',
                'ON_LARGEDAMAGE_HEAL_RELATIVE': 'Recurrent Crashing Renovator',
                'ON_HP30_HEAL_ABSOLUTE': 'Recurrent Emergency Repairer',
                'ON_HP30_HEAL_RELATIVE': 'Recurrent Emergency Renovator', 'AFTER_PHASESHIFT_HEAL': 'Phasing Repairer',
                'EFFECT_ACCUMULATION_LOWERED': 'Control Resistor', 'DOT_DAMAGE_LOWERED': 'Anti-Acid',
                'ON_DAMAGE_SUPPRESSION': 'In-trouble Suppressor', 'ON_DAMAGE_FREEZE': 'In-trouble Freezer',
                'ON_DAMAGE_DEATHMARK': 'In-trouble Death Mark', 'ON_SHOOTING_ROOT_CHARGE': 'Lockdowner',
                'ON_SHOOTING_FREEZE_CHARGE': 'Freezer', 'ON_SHOOTING_SUPPRESSION_CHARGE': 'Suppressor',
                'DRONE_PENETRATION': 'Defence Mitigator', 'DRONE_DOT': 'Acid Sprayer',
                'DRONE_MINIGUN': 'Target-seeking Minigun Shooter', 'DRONE_CANON': 'Target-seeking Canon Shooter',
                'DRONE_RIFLE': 'Imitating Rifle Shooter', 'DRONE_MINIROCKET': 'Imitating Rocket Shooter',
                'BATTERY_MICROCHIP': 'Battery Microchip'}

    papirus3 = {'Damage':'Damage', 'Cooldown':'Cooldown', 'HP': 'Durability', 'Shield': "Shield",
                'Speed': 'Speed', 'GatchaKeys': 'Keys', 'Honor': 'Honor', 'Silver': 'Silver'}

    kawaii = (i['content'].split('\t')[0]).split(' ')
    content_list = ['content0', 'content1', 'content2', 'content3', 'content4', 'content5']
    offer = []
    kawaii_list = [kawaii]

    for item in content_list:
        if item in i.keys() and i[item] != '':
            kawaii_list.append((i[item].split('\t')[0]).split(' '))

    # if 'content0' in i.keys() and i['content0'] != '':
    #     kawaii_list.append((i['content0'].split('\t')[0]).split(' '))
    # if 'content1' in i.keys() and i['content1'] != '':
    #     kawaii_list.append((i['content1'].split('\t')[0]).split(' '))
    # if 'content2' in i.keys() and i['content2'] != '':
    #     kawaii_list.append((i['content2'].split('\t')[0]).split(' '))
    # if 'content3' in i.keys() and i['content3'] != '':
    #     kawaii_list.append((i['content3'].split('\t')[0]).split(' '))
    # if 'content4' in i.keys() and i['content4'] != '':
    #     kawaii_list.append((i['content4'].split('\t')[0]).split(' '))
    # if 'content5' in i.keys() and i['content5'] != '':
    #     kawaii_list.append((i['content5'].split('\t')[0]).split(' '))

    for item in kawaii_list:
        if item[0] == 'Валюта':
            offer.append(f'{item[2]} {papirus[item[1]]}')
        elif item[0] == 'Робот' or item[0] == 'Экипировка':
            offer.append(f'{item[1][:-3]}')
        elif item[0] == 'Скин':
            offer.append(f'{item[1].capitalize()} Paintjob')
        elif item[0] == 'Дрон':
            offer.append(item[1].split("'")[1])
        elif item[0] == 'Chip':
            title = papirus1[item[1].split("'")[1][:-3]]
            title1 = item[1].split("'")[1][-2:]
            offer.append(f'{title1} {title}')
        elif item[0] == 'Баффы':
            for key in papirus3:
                if item[3].find(key) != -1:
                    offer.append(f'{item[1]} {papirus3[key]} boosters')
        elif item[0] == 'Титан':
            offer.append(f'{item[1][:-4]}')
        elif item[0] == 'Battle':
            offer.append(f'Operation Pass')
        elif item[0] == 'Премиум':
            offer.append(f'{item[1]} h of Premium')
        elif item[0] == 'BS':
            offer.append(f'{item[2]} OXP boosters')

    return offer


for i in dicks:
    k = find_sku_code()
    nani = ', '.join(find_content())
    file_result.writelines(f"{i['date'][3:13]} - {k} - {nani} \n")

file_result.close()
file_orig.close()