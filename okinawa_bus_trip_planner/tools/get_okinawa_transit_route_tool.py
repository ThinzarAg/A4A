from google.adk.tools.function_tool import FunctionTool

def get_okinawa_transit_route(destination: str, origin: str = "那覇空港") -> str:
    \"\"\"
    指定された目的地までの公共交通機関（バス・モノレール）を使用したGoogle Mapsのルート検索リンクを生成します。
    
    Args:
        destination: 目的地の名称（例：美ら海水族館、アメリカンビレッジ）
        origin: 出発地の名称（デフォルトは「那覇空港」）
        
    Returns:
        Google Mapsのルート検索URL（公共交通機関モード）
    \"\"\"
    from urllib.parse import quote
    
    base_url = "https://www.google.com/maps/dir/?api=1"
    encoded_origin = quote(origin)
    encoded_destination = quote(destination)
    
    # travelmode=transit を指定することで公共交通機関のルートを表示
    maps_url = f"{base_url}&origin={encoded_origin}&destination={encoded_destination}&travelmode=transit"
    
    return maps_url


# FunctionToolとして登録
get_okinawa_transit_route_tool = FunctionTool(func=get_okinawa_transit_route)
