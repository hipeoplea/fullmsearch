import distance


def get_scale(result):
    result_js = result.json()
    toponym = result_js["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    toponym_obj = toponym["boundedBy"]["Envelope"]
    a = [float(x) for x in toponym_obj['lowerCorner'].split()]
    b = [float(x) for x in toponym_obj['upperCorner'].split()]
    dist = distance.lonlat_distance(a, b) / (111 * 1000)
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(dist), str(dist)]),
        "l": f"=map&pt={','.join([toponym_longitude, toponym_lattitude])}"
    }
    return map_params
