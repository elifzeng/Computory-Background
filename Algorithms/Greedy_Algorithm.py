# 创建列表，包含要覆盖的州，将其传入并转换为一个集合set()。（set不包含重复元素，会自动去重）
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# 可供选择的广播台清单,所有键对应的值都是集合
# 注意，广播台覆盖的州不一定是我们需要覆盖的州
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
# 用一个集合储存最终选择的广播台
final_stations = set()

while states_needed:  # 一直循环，直到所有州都被覆盖
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # 求交集，即广播台已包含的，需要覆盖的州
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered
print(final_stations)
