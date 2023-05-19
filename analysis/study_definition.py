from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA

teratogenic_drug_codes = codelist_from_csv(
    "codelists/opensafely-teratogenic-medicines.csv",
    system="snomed",
    column="dmd_id")

as_of_date = "2019-09-01"

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    # the line below means I am interested with patients who
    # haven't changed practices between these two dates
    population=patients.registered_with_one_practice_between(
        "2019-02-01", "2020-02-01"
    ),

    # give the age of each patient on a given data and 
    # I expect every patient to have an age that matches 
    # the UK population
    age=patients.age_as_of(
        as_of_date,
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        }
    ),

    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),

    imd=patients.address_as_of(
        as_of_date,
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"100": 0.1, "200": 0.2, "300": 0.7}},
        }
    ),

    teratogenics=patients.with_these_medications(
        teratogenic_drug_codes,
        return_expectations={
           "int": {"distribution": "normal", "mean": 2, "stddev": 1},
           "incidence": 0.2,
        },
        on_or_before=None,
        on_or_after=None,
        between=["2010-04-01", "2023-03-31"],
        find_first_match_in_period=None,
        find_last_match_in_period=None,
        returning="number_of_matches_in_period",
        include_date_of_match=True,
        date_format=None,
        ignore_days_where_these_clinical_codes_occur=None,
        episode_defined_as=None,
        return_binary_flag=None,
        return_number_of_matches_in_period=False,
        return_first_date_in_period=False,
        return_last_date_in_period=False,
        include_month=False,
        include_day=False)

)
