# Парсинг текстового представления заявки для выдачи списка ссылок
# на файлы из minio

TEXT = """
{
    "passport_main": "/media/193434",
    "passport_registration": "/media/193435",
    "passport_old_page": null,
    "pension_photo": null,
    "validation_code": "4922",
    "sms_count": 1,
    "sms_time": "2023-07-10T11:36:03+03:00",
    "enter_valid_code_time": "2023-07-10T11:36:27+03:00",
    "exchange_error": null,
    "doc_error": "null",
    "antifraud_time": "2023-07-10T11:37:01+03:00",
    "exchange_date": "2023-07-10T11:44:40+03:00",
    "card_barcode": "1830133826579",
    "product_consent": true,
    "operation_count": 50000,
    "statement_link": "https://documents.finmarket.online/media/64abc226e2642c2fb67dc04a-st-64abc332e8f3b104213864.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=saturn_crm%2F20230710%2F%2Fs3%2Faws4_request&X-Amz-Date=20230710T083707Z&X-Amz-SignedHeaders=host&X-Amz-Expires=604800&X-Amz-Signature=a72993675e366d97aeb8751c824f4c38335116233fcc802ea8fd07fc16f61b68",
    "statement": "/media/193449",
    "signed_statement": "/media/193465",
    "code_word": "Татьяна",
    "kbo_number": "ФФТ00001138/23",
    "verification_id": "1-454N0WCH",
    "card_num": "220026xxxxxx2857",
    "account_num": "40817810005140000375",
    "passport_main_update": null,
    "passport_registration_update": null,
    "pension_photo_update": null,
    "passport_old_page_update": null,
    "signed_statement_update": null,
    "attachment_link": "https://documents.finmarket.online/media/64abc226e2642c2fb67dc04a-at-64abc467942d6702887096.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=saturn_crm%2F20230710%2F%2Fs3%2Faws4_request&X-Amz-Date=20230710T084215Z&X-Amz-SignedHeaders=host&X-Amz-Expires=604800&X-Amz-Signature=438717e45876380b28fb8756b6bf13a2b63e4ad68b5599da477b4a01ef33a560",
    "attachment": "/media/193468",
    "signed_attachment": "/media/193474",
    "attachment_count": 1,
    "id": "64abc226e2642c2fb67dc04a",
    "owner_id": 42416,
    "created_date": "2023-07-10T11:32:38+03:00",
    "client_id": "64abc224d45960579557facf",
    "remote_id": "64abc226e2642c2fb67dc04a",
    "deleted_date": null,
    "lifecycle_state": "created",
    "wizard_state": "completed",
    "utm": {
        "utm_source": "finbrokerweb",
        "utm_medium": "finbrokerweb",
        "utm_campaign": "finbrokerweb",
        "utm_content": "finbrokerweb",
        "utm_term": "finbrokerweb"
    },
    "transition_history": {
        "hash_storage": {
            "enter_contact_data": "6c7282c657d528cb25958e92e716d6fe",
            "enter_passport_data": "d751713988987e9331980363e24189ce",
            "enter_validation_code": "2f4674950a0754ca997c79d3e74eafe6",
            "enter_card_data": "6fe7946767e1119298f78c54712e7048",
            "enter_consent_data": "fbfdff1e155b5ef9e0fc96474fecb816",
            "enter_statement_data": "fb5230cfdafca65eb34b9452919e2919",
            "enter_attachment_data": "f7dd13fdfb71a005a7e2e88352eb238e"
        },
        "entries": [
            {
                "trigger": "commit_action",
                "transition_user": 42416,
                "transition_date": "2023-07-10T11:34:49+03:00",
                "transition": "enter_contact_data"
            },
            {
                "trigger": "commit_action",
                "transition_user": 42416,
                "transition_date": "2023-07-10T11:36:03+03:00",
                "transition": "enter_passport_data"
            },
            {
                "trigger": "commit_action",
                "transition_user": 42416,
                "transition_date": "2023-07-10T11:36:27+03:00",
                "transition": "enter_validation_code"
            },
            {
                "trigger": "commit_action",
                "transition_user": 42416,
                "transition_date": "2023-07-10T11:36:46+03:00",
                "transition": "enter_card_data"
            },
            {
                "trigger": "commit_action",
                "transition_user": 42416,
                "transition_date": "2023-07-10T11:37:01+03:00",
                "transition": "enter_consent_data"
            },
            {
                "trigger": "commit_action",
                "transition_user": 42416,
                "transition_date": "2023-07-10T11:39:37+03:00",
                "transition": "enter_statement_data"
            },
            {
                "trigger": "commit_action",
                "transition_user": 42416,
                "transition_date": "2023-07-10T11:44:39+03:00",
                "transition": "enter_attachment_data"
            }
        ],
        "latest_update": "2023-07-10T11:44:39+03:00"
    },
    "rules": [],
    "status": {
        "raw_value": "act",
        "value": "ACTIVATED"
    },
    "generated": [
        {
            "level": 0,
            "value": "Активирована"
        },
        {
            "level": 10,
            "value": "Успешная продажа "
        },
        {
            "level": 100,
            "value": "Карта выдана"
        }
    ],
    "readable": [],
    "registry": {
        "meta": {
            "version": "e91f1f2c070851f62607938634596176",
            "snapshot": {
                "city_mkb": "/registry/attribute/city_mkb",
                "passport_lastname": "/registry/attribute/passport_lastname",
                "passport_name": "/registry/attribute/passport_name",
                "passport_middlename": "/registry/attribute/passport_middlename",
                "no_middlename": "/registry/attribute/no_middlename",
                "birth_date": "/registry/attribute/date",
                "gender": "/registry/attribute/gender",
                "personal_phone": "/registry/attribute/phone",
                "e_mail": "/registry/attribute/e_mail",
                "pension_number": "/registry/attribute/pension_number",
                "pension_date": "/registry/attribute/date",
                "change_passport": "/registry/attribute/change_passport",
                "passport": "/registry/attribute/passport",
                "previous_passport_seria": "/registry/attribute/passport_seria",
                "previous_passport_number": "/registry/attribute/passport_number",
                "previous_passport_police_code": "/registry/attribute/passport_police_code",
                "previous_passport_date": "/registry/attribute/date",
                "birth_place": "/registry/attribute/birth_place",
                "passport_address": "/registry/attribute/address",
                "current_address_optional": "/registry/attribute/current_address_optional",
                "current_address": "/registry/attribute/address"
            }
        }
    },
    "antifraud_ticket": {
        "pipeline_id": "113967",
        "pipeline_state": "ACCEPT"
    },
    "post_moderation_ticket": null,
    "moderation_ticket": null,
    "city_mkb": "rostov_na_donu",
    "passport_lastname": "БАБЕНКО",
    "passport_name": "ТАТЬЯНА",
    "passport_middlename": "МИХАЙЛОВНА",
    "no_middlename": false,
    "birth_date": "1967-07-02T00:00:00+03:00",
    "gender": "f",
    "personal_phone": "79615061837",
    "e_mail": null,
    "pension_number": null,
    "pension_date": null,
    "change_passport": null,
    "passport": {
        "passport_seria": "0312",
        "passport_number": "131107",
        "passport_date": "2012-09-27T00:00:00+04:00",
        "passport_police": "ОТДЕЛЕНИЕМ УФМС ПО КРАСНОДАРСКОМУ КРАЮ В КУЩЕВСКОМ РАЙОНЕ",
        "passport_police_code": "230-041"
    },
    "previous_passport_seria": null,
    "previous_passport_number": null,
    "previous_passport_police_code": null,
    "previous_passport_date": null,
    "birth_place": "СТ КУЩЕВСКАЯ КРАСНОДАРСКОГО КРАЯ",
    "passport_address": {
        "building": "155",
        "corpus": null,
        "district": null,
        "district_type": null,
        "flat": null,
        "place": null,
        "place_type": null,
        "postalcode": "352030",
        "region": "Краснодарский",
        "region_type": "край",
        "service_address": "352030, Краснодарский край, Кущевский р-н, ст-ца Кущевская, ул Кирова, д 155",
        "service_fias_code": null,
        "service_fias_id": "2ae8f13b-7612-4203-b037-2c7e11d37daf",
        "service_fias_level": 8,
        "service_kladr_id": "2302000000100490019",
        "service_place_fias_id": null,
        "service_place_kladr_id": null,
        "service_qc_geo": 0,
        "service_subplace_fias_id": null,
        "service_subplace_kladr_id": null,
        "street": "Кирова",
        "street_type": "ул",
        "subplace": "Кущевская",
        "subplace_type": "ст-ца"
    },
    "current_address_optional": true,
    "current_address": {
        "building": "155",
        "corpus": null,
        "district": null,
        "district_type": null,
        "flat": null,
        "place": null,
        "place_type": null,
        "postalcode": "352030",
        "region": "Краснодарский",
        "region_type": "край",
        "service_address": "352030, Краснодарский край, Кущевский р-н, ст-ца Кущевская, ул Кирова, д 155",
        "service_fias_code": null,
        "service_fias_id": "2ae8f13b-7612-4203-b037-2c7e11d37daf",
        "service_fias_level": 8,
        "service_kladr_id": "2302000000100490019",
        "service_place_fias_id": null,
        "service_place_kladr_id": null,
        "service_qc_geo": 0,
        "service_subplace_fias_id": null,
        "service_subplace_kladr_id": null,
        "street": "Кирова",
        "street_type": "ул",
        "subplace": "Кущевская",
        "subplace_type": "ст-ца"
    },
    "_generated_": [
        {
            "level": 0,
            "value": "Активирована"
        },
        {
            "level": 10,
            "value": "Успешная продажа "
        },
        {
            "level": 100,
            "value": "Карта выдана"
        }
    ]
}"""

for line in TEXT.split('\n'):
    if len(line.split('/media/')) > 1:
        if line.find('consent_link') > -1: #and line.find('.pdf') < line.split('/media/')[1].split('"')[0]:
            media_link = line.split('"')[3].split('"')[0]
        else:
            media_link = 'https://eva.finmarket.online/media/download/' + line.split('/media/')[1].split('"')[0]
        print(media_link)
        off = '''
        while not downloaded:
            try:
                answer = requests.get(media_link)
            except Exception as e:
                repit += 1
                errors[int(file['id'])] = e
                if repit > MAX_REPIT:
                    skipping = True
                    break
                else:
                    continue
            if answer.reason == 'Not Found' or answer.reason == 'Forbidden':
                downloaded_files_ids += [int(file['id'])]
                skipping = True
                break
            if not answer.ok:
                repit += 1
                errors[int(file['id'])] = answer.reason
                if repit > MAX_REPIT:
                    downloaded_files_ids += [int(file['id'])]
                    skipping = True
                    break
            downloaded = answer.ok
        '''
