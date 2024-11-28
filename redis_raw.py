import redis

redis_conn = redis.Redis(host='localhost', port=6379, db=0)

redis_conn.set('chave_1', 'trocando_o_meu_valor')

meu_valor = redis_conn.get('chave_1').decode('utf-8')

redis_conn.delete('chave_1')

meu_hash = { # Chave de exemplo
    'name': 'felipe',
    'age': 25,
    'city': 'São Paulo'
}
redis_conn.hset('meu_hash', 'name', 'felipe')
redis_conn.hset('meu_hash', 'age', 25)
redis_conn.hset('meu_hash', 'city', 'São Paulo')

redis_conn.hdel('meu_hash', 'city')


# Buscas por existências
elem = redis_conn.exists('chave_1')
print(elem)
elem_2 = redis_conn.exists('meu_hash')
print(elem_2)
elem_3 = redis_conn.hexists('meu_hash', 'name')
print(elem_3)
elem_4 = redis_conn.hexists('meu_hash', 'city')
print(elem_4)

redis_conn.set('chave_del', 'valor que irá ser deletado', ex=10)