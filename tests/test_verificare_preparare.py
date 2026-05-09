from app.lib.biblioteca_gastronomie import get_preparare

def test_verificare_preparare():
    assert "Pentru început, se presează amestecul de biscuiți și unt în tavă pentru a forma blatul. Separat, se mixează crema de brânză cu zahărul, ouăle și vanilia. Crema se toarnă peste blat, iar prăjitura se coace (adesea la baie de aburi) până se încheagă marginile. Se lasă la răcit la frigider peste noapte." in get_preparare()
