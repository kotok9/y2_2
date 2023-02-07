import sys

from geocoder import geocoder_get_ll_spn, show_map_save

toponym_to_find = " ".join(sys.argv[1:])

ll, spn = geocoder_get_ll_spn(toponym_to_find)

ll_spn = f"ll={ll}&spn={spn}"
add_param = f"pt={ll},pmwtm1"

show_map_save(ll_spn=ll_spn, add_params=add_param)
