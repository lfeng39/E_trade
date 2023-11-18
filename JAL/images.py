from importlib.resources import path
from operator import imod
import os
from JAL import models


print('>>> this is images.py <<<')

# data列表
# _asin_ = ['B09KG4R3YR', 'B09YLKWBMV', 'B09YLLXKDT', 'B0BFHQTG6R']
# _asin_ = models.Products.getAsin()
_version_ = ['v1.00', 'v1.01', 'v1.02']
_folder_ = ['7', '970', '300']

'''
构建每个asin下的图片路径
例如 'static/image/B09YLLXKDT/v1.00/7'
最终将路径对应到asin下 以字典的形式存储
例如 'B09YLLXKDT': ['static/image/B09YLLXKDT/v1.00/7',
                    'static/image/B09YLLXKDT/v1.00/970',
                    'static/image/B09YLLXKDT/v1.00/300']
'''
# 以字典形式，返回asin下三个文件夹内的图片路径
# path: 'static/image/B09YLLXKDT/v1.00/7/'
def pathAsinImg(_asin_):

    '''
    paths_asin_img_dict = {
        'asins':['asin/version/folder/',],
    }
    '''

    # 按文件夹folder构建路径，并存储到列表
    paths_img = []
    # 将paths_img列表中，每个子列表对应到对应的asin，并以字典形式存储
    paths_asin_img_dict = {}
    for k in range(len(_asin_)):
        paths_img.append([])
        for i in range(len(_folder_)):
            # 将7、970、300的路径循环进paths_img对应的列表
            paths_img[k].append('static/image/products/' + _asin_[k] + '/' + _version_[0] + '/' + _folder_[i] + '/')
            # 将每个asin下的7、970、300路径列表循环进paths_asin_img_dict字典
            paths_asin_img_dict[_asin_[k]] = paths_img[k]
    
    return paths_asin_img_dict


# url: '/static/image/B09YLLXKDT/v1.00/7/Listing-1.jpg'
def urlAsinImg(_asin_):
    '''
    urls_asin_img_dict = {
        'asins':{ 'folder': ['/asin/version/folder/files_name',], },
    }
    '''
    # files_name_list = [['A+-970-01.jpg', 'A+-970-03.jpg', 'A+-970-02.jpg'],[],[]]
    files_name_list = []
    urls_asin_img_dict = {}
    for i in range(len(_asin_)):
        files_name_list.append([])
        for k in range(len(_folder_)):
            # 获取图片名称，并添加至对应文件夹列表
            files_name = os.listdir(pathAsinImg(_asin_)[_asin_[i]][k])
            
            # 删除MacOs系统下，改变图片名称，自动生成的隐藏文件'.DS_Store'
            # 将图片排序，名称开头包含1的图片，放在列表第一位
            for item in files_name:
                if item == '.DS_Store':
                    files_name.remove(item)
                # elif item[0] == '1':
                #     files_name.insert(0, item)
                #     break
                else:
                    pass

            # 将过滤后的图片列表添加至目标列表
            files_name_list[i].append(files_name)
        
        urls_asin_img_dict[_asin_[i]] = {'7':[],'970':[],'300':[]}
    
    for v in range(len(_asin_)):
        for k in range(len(_folder_)):
            for i in  range(len(files_name_list[v][k])):
                urls_asin_img_dict[_asin_[v]][_folder_[k]].append('/' + pathAsinImg(_asin_)[_asin_[v]][k] + files_name_list[v][k][i])

    return urls_asin_img_dict

# asin_db_list = data_source.AsinDB.asinList
# print(urlAsinImg(asin_db_list))



'''
creat img url from folder, the data don't save to DB
get url object by asin and type
the type is: 7 | 970 | 300
'''
class Img:
    '''
    Create img path
    '''
    def imgPath(asin, type):
        img_path = 'static/image/products/' + asin + '/v1.00/' + type + '/'
    
        return img_path
    
    '''
    ImgPath is key, imgFile is values
    '''
    def imgDict(asin, type):
        img_file_list = os.listdir(Img.imgPath(asin, type))
        if '.DS_Store' in img_file_list:
            img_file_list.pop(img_file_list.index('.DS_Store'))

        product_img_dict = {
            'img_path' : Img.imgPath(asin, type),
            'img_file_list' : img_file_list
        }

        return product_img_dict
    
    '''
    Create img url
    '''
    def imgUrl(asin, type):
        img_url = []
        for url in Img.imgDict(asin, type)['img_file_list']:
            url = Img.imgPath(asin, type) + url
            img_url.append(url)

        return img_url
    
    '''
    Get first img from img_file_list by method os.lisdir(), and create url with first img
    '''
    def firstImg(asin, type):
        for img_file in os.listdir(Img.imgPath(asin, type)):
            if img_file.startswith('00-'):
                first_img = '/' + Img.imgPath(asin, type) + img_file
                return first_img

'''
test print 
'''
# print(Img.firstImg('B0BGHBW13S', '7'))

# for file in os.listdir(Img.imgPath('B0BGHBW13S', '7')):
#     print(file)


