spice_mix = set()
nst = set()
nst.add("normal stuff")
print(f"initial spice mix id : {id(spice_mix)}")
spice_mix.add("cardamom")
spice_mix.add("ginger")
print(f"after spice mix id : {id(spice_mix)}")

spice_mix = nst

print(f"after spice mix id : {id(spice_mix)}")

