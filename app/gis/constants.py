RUBRICS_FILE_POSSIBLE_KEYS = {
    "rubrics_file",
    "rubric_file",
}
RUBRICS_CODES_POSSIBLE_KEYS = {
    "rubrics_codes",
    "rubric_codes",
    "rubrics_ids",
    "rubric_ids",
}

CITIES_FILE_POSSIBLE_KEYS = {
    "cities_file",
    "city_file",
}
CITIES_IDS_POSSIBLE_KEYS = {
    "cities_ids",
    "city_ids",
    "cities_codes",
    "city_codes",
}

QUERIES_FILE_POSSIBLE_KEYS = {"queries_file"}

QUERY_POSSIBLE_KEYS = {"query"}

PARSE_REVIEWS_POSSIBLE_KEYS = {
    "parse_reviews",
}

PARSE_MENUS_POSSIBLE_KEYS = {
    "parse_menus",
}

PARSE_MEDIA_POSSIBLE_KEYS = {
    "parse_media",
}

CONFLICTING_KEYS = {
    "rubrics": RUBRICS_FILE_POSSIBLE_KEYS.union(RUBRICS_CODES_POSSIBLE_KEYS).union(
        {"parse_all_rubrics"}
    ),
    "cities": CITIES_FILE_POSSIBLE_KEYS.union(CITIES_IDS_POSSIBLE_KEYS).union(
        {"country", "parse_all_cities"}
    ),
    "queries": QUERIES_FILE_POSSIBLE_KEYS.union(QUERY_POSSIBLE_KEYS),
    "parse_reviews": PARSE_REVIEWS_POSSIBLE_KEYS,
    "parse_menus": PARSE_MENUS_POSSIBLE_KEYS,
    "parse_media": PARSE_MEDIA_POSSIBLE_KEYS,
}


TRUE_VARIATIONS = {"true", "1", "yes", "y", "t"}


FIELDS = [
    "ad",
    "cb",
    "context_rubrics",
    "dym",
    "items.access_comment",
    "items.access",
    "items.address",
    "items.adm_div",
    "items.ads.options",
    "items.ads",
    "items.alias",
    "items.attribute_groups",
    "items.barrier",
    "items.capacity",
    "items.city_alias",
    "items.comment",
    "items.congestion",
    "items.contact_groups",
    "items.context",
    "items.dates.created_at",
    "items.dates.deleted_at",
    "items.dates.updated_at",
    "items.dates",
    "items.delivery",
    "items.description",
    "items.detailed_subtype",
    "items.directions",
    "items.email_for_sending.allowed",
    "items.external_content",
    "items.flags",
    "items.floor_id",
    "items.floor_plans",
    "items.floors",
    "items.for_trucks",
    "items.full_address_name",
    "items.geometry.centroid",
    "items.geometry.hover",
    "items.geometry.selection",
    "items.geometry.style",
    "items.group",
    "items.has_ads_model",
    "items.has_apartments_info",
    "items.has_discount",
    "items.has_dynamic_congestion",
    "items.has_exchange",
    "items.has_goods",
    "items.has_otello_hotels",
    "items.has_otello_stories",
    "items.has_payments",
    "items.has_pinned_goods",
    "items.has_realty",
    "items.inactive",
    "items.is_incentive",
    "items.is_paid",
    "items.is_promoted",
    "items.is_routing_available",
    "items.level_count",
    "items.links",
    "items.locale",
    "items.metarubrics",
    "items.name_back",
    "items.name_ex",
    "items.order_with_cart",
    "items.org",
    "items.paving_type",
    "items.platforms",
    "items.poi_category",
    "items.point",
    "items.purpose_code",
    "items.purpose",
    "items.reg_bc_url",
    "items.region_id",
    "items.reply_rate",
    "items.reviews",
    "items.route_logo",
    "items.routes",
    "items.rubrics",
    "items.schedule_special",
    "items.schedule",
    "items.search_attributes.additional_info",
    "items.search_attributes.best_keyword",
    "items.search_attributes.detection_type",
    "items.search_attributes.dgis_ad_rubric_id",
    "items.search_attributes.dgis_ad_type",
    "items.search_attributes.dgis_found_by_address",
    "items.search_attributes.dgis_source_type",
    "items.search_attributes.personal_priority",
    "items.search_attributes.relevance",
    "items.segment_id",
    "items.ski_lift",
    "items.ski_track",
    "items.sources",
    "items.stat",
    "items.stop_factors",
    "items.structure_info.elevators_count",
    "items.structure_info.floor_type",
    "items.structure_info.gas_type",
    "items.structure_info.is_in_emergency_state",
    "items.structure_info.material",
    "items.structure_info.project_type",
    "items.structure_info.year_of_construction",
    "items.subtype",
    "items.temporary_unavailable_atm_services",
    "items.timezone_offset",
    "items.timezone",
    "items.vacancies",
    "query_context",
    "request_type",
    "search_attributes",
    "search_type",
]

RUBRICS_WITH_PRICE_TAB = {
    "178",
    "305",
    "652",
    "5603",
    "382",
    "651",
    "110355",
    "58858",
    "20165",
    "13102",
    "13726",
    "56759",
    "14942",
    "69989",
    "13597",
    "51009",
    "53986",
    "70190",
    "67142",
    "50870",
    "110479",
    "110353",
    "110351",
    "110352",
    "69491",
    "110975",
    "110998",
    "405",
    "7689",
    "205",
}
RUBRICS_WITH_MENU_TAB = {
    "161",
    "164",
    "159",
    "1203",
    "9786",
    "21501",
    "58871",
    "110317",
    "110408",
    "165",
    "162",
    "110411",
    "51459",
    "110376",
    "52248",
    "166",
    "15791",
    "111593",
    "363",
    "469",
    "879",
    "10803",
    "111594",
    "112656",
    "112658",
    "21387",
    "558",
    "16677",
}


LIST_URL_TEMPLATE = (
    "https://catalog.api.2gis.ru/2.0/catalog/branch/list"
    "?page={page}"
    "&page_size={per_page}"
    "&rubric_id={rubric_id}"
    "&region_id={city_id}"
    f"&fields={','.join(FIELDS)}"
    "&key=rutnpt3272"
)
SEARCH_URL_TEMPLATE = (
    "https://catalog.api.2gis.ru/2.0/catalog/branch/search"
    "?page={page}"
    "&page_size={per_page}"
    "&q={query}"
    "&region_id={city_id}"
    f"&fields={','.join(FIELDS)}"
    "&key=rutnpt3272"
)
REVIEWS_URL_TEMPLATE = "https://public-api.reviews.2gis.com/3.0/branches/{org_id}/reviews?limit={per_page}&offset={offset}&is_advertiser=false&fields=meta.providers,meta.branch_rating,meta.branch_reviews_count,meta.total_count,reviews.hiding_reason,reviews.emojis,reviews.trust_factors&without_my_first_review=false&rated=true&sort_by=friends&key=6e7e1929-4ea9-4a5d-8c05-d601860389bd"
MENUS_URL_TEMPLATE = "https://market-backend.api.2gis.ru/5.0/product/items_by_branch?branch_id={org_id}&page={page}&page_size={per_page}&feature_config=categories_without_fake_first_level,range_price_type_supported,from_price_type_supported,fas_not_ad_text"
MEDIA_URL_TEMPLATE = "https://api.photo.2gis.com/3.0/objects/{org_id}/albums/{album_type}/media?key=gYu1s9N1wP&page_size={per_page}"
