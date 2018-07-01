from openfisca_barcelona.entities import *
from openfisca_core.model_api import *


class es_ocupant_dun_habitatge_gestionat_per_lagencia_de_lhabitatge(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "The house is property of agencia de l'habitatge"
    default_value = False


class existeix_deute_en_el_pagament_de_la_hipoteca(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "A debt in the mortage exists"
    default_value = False


class existeix_deute_en_el_pagament_del_lloguer(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "A debt in the rent exists"
    default_value = False


class fa_mes_de_12_mesos_que_existeix_el_deute_de_hipoteca(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "The debt has existed for more than 12 months"
    default_value = False


class ha_pagat_almenys_3_quotes_del_lloguer(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "A debt in the rent exists"
    default_value = False


class ha_perdut_lhabitatge_en_els_ultims_2_anys(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "The user has been evicted in the last 2 years"
    default_value = False


class ha_pagat_12_mesos_daquesta_hipoteca(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "A debt in the rent exists"
    default_value = False


class ha_participat_en_un_proces_de_mediacio(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "The user has participated in a mediation process between owner and administration"
    default_value = False


class ha_rebut_oferta_per_accedir_a_habitatge_i_lha_rebutjada(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "The user has received an offer for a house and has declined"
    default_value = False


class import_del_lloguer(Variable):
    value_type = float
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "rent amount"
    default_value = 0


class import_de_la_hipoteca(Variable):
    value_type = float
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "Mortage amount"
    default_value = 0


class relacio_de_parentiu_amb_el_propietari(Variable):
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "Some person has a familiar relation to the owner"
    default_value = False


class tempsEmpadronatHabitatgeActual(Enum):
    no_empadronat = "no_empadronat"
    menys_nou_mesos = "menys_9_mesos"
    nou_mesos_o_mes = "9_mesos_o_mes"


class temps_empadronat_habitatge_actual(Variable):
    value_type = Enum
    possible_values = tempsEmpadronatHabitatgeActual
    default_value = tempsEmpadronatHabitatgeActual.no_empadronat
    entity = Persona
    label = u"labor situation"
    definition_period = MONTH


class tinc_alguna_propietat_a_part_habitatge_habitual_i_disposo_dusdefruit(Variable):
    default_value = False
    value_type = bool
    entity = UnitatDeConvivencia
    definition_period = MONTH
    label = "Some person living in the house has a property"


def clauIRSCPonderat(membres):
    return select([membres == 1, membres == 2, membres == 3, membres > 3],
                  ['un', 'dos', 'tres', 'quatreomes'])


def clauMultiplicadors(membres, existeixDiscapacitat):
    return select([existeixDiscapacitat, membres == 1, membres >= 2],
                  ['discapacitats', 'un', 'dosomes']
                  )
