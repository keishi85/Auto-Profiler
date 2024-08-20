import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
"""
    取得したデータから画像生成を行うプログラム
    引数: 取得したデータ(key: value)
    返り値: profile(バイナリデータ)
"""
def generate_profile(data: dict)->bytes:
    # 画像生成処理
    pass


"""
    入力された国名から国の部分を作成
    引数: 国名
"""
def generate_country(country_name: str)->None:
    # 手動でダウンロードしたシェープファイルのパスを指定
    shapefile_path = "app/static/data/map/110m_cultural/ne_110m_admin_0_countries.shp"
    world = gpd.read_file(shapefile_path)

    # 座標系の確認と変換
    if world.crs is None:
        print("シェープファイルの座標系が未設定です。")
        world = world.set_crs(epsg=4326, allow_override=True)
    else:
        print(f"元の座標系: {world.crs}")
        if world.crs != 'EPSG:4326':
            world = world.to_crs(epsg=4326)
            print("座標系をEPSG:4326に変換しました。")

    # 国名カラムの確認
    world['country_name_lower'] = world['NAME'].str.lower()
    country_shape = world[world['country_name_lower'] == country_name.lower()]
    print(country_shape)

    if country_shape.empty:
        print(f"{country_name.capitalize()} という国は見つかりませんでした。")
        print("利用可能な国名リスト:", world['NAME'].unique())
    else:
        # 国の重心を取得
        country_centroid = country_shape.geometry.centroid.iloc[0]

        # 地図の描画
        fig, ax = plt.subplots(figsize=(15, 10),
                               subplot_kw={'projection': ccrs.PlateCarree(central_longitude=150)})

        # 世界地図全体を表示
        ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

        # 国を薄い紫色で塗りつぶし、境界線を表示しない
        ax.add_geometries(world['geometry'], crs=ccrs.PlateCarree(), facecolor='lavender', edgecolor='none')

        # 国の中心に赤い点を打つ（投影法を指定）
        ax.plot(country_centroid.x, country_centroid.y, 'ro', markersize=10, transform=ccrs.PlateCarree())

        # 目盛りを消す
        ax.axis('off')

        plt.savefig("country.png", bbox_inches='tight', pad_inches=0)