def fetch_and_cache_data(func, cache_key, to_table_oriented_json=False):
    cached_data = REDIS_CONN.get(cache_key)
    
    if cached_data:
        prepped_data = json.loads(cached_data)
        from_cache = True
    else:
        data = func()
        if to_table_oriented_json:
            prepped_data = json.loads(data.to_json(orient='table'))
            prepped_data = prepped_data["data"]
        else:
            prepped_data = data
        REDIS_CONN.set(cache_key, json.dumps(prepped_data))
        from_cache = False

    return prepped_data, from_cache