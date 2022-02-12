import sys
from geocoder import get_ll_span, get_nearest_organization
from mapapi import show_map
from distance import lonlat_distance


def main(toponim):
    ll = get_ll_span(toponim)[0]
    pt0 = ll + ',pmdom1'
    obj_ll, org_name, t, address = get_nearest_organization(ll.split(','), 'аптека')
    dist = round(lonlat_distance(list(map(float, ll.split(','))), obj_ll), 1)
    print(f'Name: {org_name},\nAddress: {address},\nDistance: {dist}m,\nWorking hours: {t}')
    pt = f'{obj_ll[0]},{obj_ll[1]},pmdom2'
    show_map(f'll={ll}&pt={pt0}~{pt}')


if __name__ == '__main__':
    t = " ".join(sys.argv[1:])
    if t:
        main(t)
