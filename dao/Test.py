import PositionDAO
from model.Position import Position
import json

position = PositionDAO.findPositionById(3)

print json.dumps(vars(position),sort_keys=True, indent=4)
