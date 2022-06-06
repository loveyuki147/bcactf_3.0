# Crappy Colonization Corp
225 points - By skysky

Tag: crypto, rev

Yay, we finally got someone to Mars! It's bureaucracy time!

[provided.rs](provided.rs)

`nc crypto.bcactf.com 49157`

## Hint
- Your IGUID is not used as an index into the hashmap. Only the result of the "proprietary algorithm" is used.
- Although your IGUID is not used as an index into the hashmap... it is still stored as a vector of bytes in "used_keys".
- How proprietary is this "proprietary algorithm", anyway?

## Write up