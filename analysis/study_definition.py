from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA


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
        "2019-09-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        }
    )
)
