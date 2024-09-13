select count(*) as FISH_COUNT from FISH_INFO i, FISH_NAME_INFO n
where i.FISH_TYPE = n.FISH_TYPE and (n.FISH_NAME = "BASS" or n.FISH_NAME = "SNAPPER");