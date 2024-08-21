docker build -t contact_list_api .
docker-compose down
docker-compose up -d
python fisrt_insert.py