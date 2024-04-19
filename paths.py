# 路径列表


# 角色等级
level_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "Level",
    "value"
]

# 角色名
NickName_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "NickName",
    "value"
]

# ???
HP_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "HP",
    "value"
]

# 角色饱食度
FullStomach_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "FullStomach",
    "value"
]

# ??? 
Support_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "Support",
    "value"
]

# 角色工作速度
CraftSpeed_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "CraftSpeed",
    "value"
]

# ???
MaxSP_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "MaxSP",
    "value",
    "Value",
    "value"
]

# 未分配属性点
UnusedStatusPoint_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "UnusedStatusPoint",
    "value"
]


#最大生命
HPStatusPoint_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "GotStatusPointList",
    "value",
    "values",
    0,
    "StatusPoint",
    "value"
]
#??
SPStatusPoint_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "GotStatusPointList",
    "value",
    "values",
    1,
    "StatusPoint",
    "value"
]
#攻击
AttackStatusPoint_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "GotStatusPointList",
    "value",
    "values",
    2,
    "StatusPoint",
    "value"
]
#负重
WeightLimitStatusPoint_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "GotStatusPointList",
    "value",
    "values",
    3,
    "StatusPoint",
    "value"
]
CaptureRateStatusPoint_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "GotStatusPointList",
    "value",
    "values",
    4,
    "StatusPoint",
    "value"
]
WorkSpeedStatusPoint_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0,  # since it's a list and we want the first item
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "GotStatusPointList",
    "value",
    "values",
    5,
    "StatusPoint"
]
#unknown
Uk1StatusPoint_hero = [
    "properties",
    "worldSaveData",
    "value",
    "CharacterSaveParameterMap",
    "value",
    0, 
    "value",
    "RawData",
    "value",
    "object",
    "SaveParameter",
    "value",
    "GotExStatusPointList",#关键在这里
    "value",
    "values",
    0,
    "StatusPoint",
    "value"
]

WorldTime = [
    #日期后面加12个0
    "properties",
    "worldSaveData",
    "value",
    "GameTimeSaveData",
    "value",
    "GameDateTimeTicks", 
    "value",
]

def Storage_hero(number):
    Storage = [
        "properties",
        "worldSaveData",
        "value",
        "ItemContainerSaveData",
        "value",
        40, 
        "value",
        "Slots",
        "value",
        "values",
        0,
        "ItemId",
        "value",
        "StaticId",
        "value"
    ]
    Storage[10] = number-1
    return Storage

def amount(array):
    index=array.index("ItemId")
    print(index)
    
    array[index] = "StackCount"
    array[index+1] = "value"
    del array[index+2:]
    return array
    