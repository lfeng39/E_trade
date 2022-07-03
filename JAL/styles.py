from . import models



def position():
    
    
    position = 'position: relative; top: 10%; left: 10%; width:50%; min-height:100px; border:1px solid #000;'

    return position


def bgContainer():

    bgContainer = {
        models.asin[0]: 'background: url(' + models.imgShower[1] + ') no-repeat; background-size: 100%; height: 790px;',
        models.asin[1]: 'background: url(' + models.imgShower[2] + ') no-repeat; background-size: 100%; height: 790px;',
        models.asin[2]: 'background: url(' + models.imgShower[0] + '); background-size: 100%; height: 790px;',
    }

    return bgContainer
