$(document).ready(function() 
{
    //Create the table
    var table = $('#kt_table').DataTable
    ( 
        {
            "ajax": 
            {
                "url": "/ajax_mission_consultant",
                "type": "GET",
                "dataType": "json",
                "async": true,
                "dataSrc": ""
            },
            "order": [[ 1, "asc" ]],
            "language": 
            {
                "url": "//cdn.datatables.net/plug-ins/1.10.20/i18n/French.json"
            },
            "columns": 
            [
                {
                    "render": function ( data, type, row )
                    {
                        var nom = row.fields.client_nom;
                        var avatar = row.fields.client_avatar;
                        var url_profil = "/administrateur/profil_client/" + row.fields.client_id;
                        if (row.fields.client_id) {
                            return (`
                            <span>
                                <div class="kt-user-card-v2">
                                    <div class="kt-user-card-v2__pic">
                                        <img src="` + avatar + `" alt="photo">
                                    </div>
                                    <div class="kt-user-card-v2__details">
                                        <a href="#" class="kt-user-card-v2__name">` + nom + `</a>
                                    </div>
                                </div>
                            </span>`);
                        }
                        else {
                            return "Non renseigné";
                        }
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var jour = row.fields.jour;
                        var debut = row.fields.debut;
                        var fin = row.fields.fin;
                        var res = '<span><div class="kt-user-card-v2"><div class="kt-user-card-v2__details">';
                        if (jour != "None")
                        {
                            var options = {year: 'numeric', month: 'long', day: 'numeric'};
                            var jour = new Date(jour)
                            res += "<span class='kt-user-card-v2__name'>" + jour.toLocaleDateString('fr-FR',options) + "</span><br>";
                        }
                        if (debut != "None" & fin != "None")
                        {
                            res += "<span class='kt-user-card-v2__desc'>" + debut + " - " + fin + "</span><br>";
                        }
                        res += '</div></div></span>'
                        return res; 
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var type = row.fields.type;
                        if (type) {
                            return type;
                        }
                        else {
                            return "Non renseigné";
                        }
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var nom = row.fields.adresse_nom;
                        var adresse = row.fields.adresse_adresse
                        var ville = row.fields.adresse_ville
                        var code = row.fields.adresse_code
                        if (nom) {
                            return (`
                            <span>
                                <div class="kt-user-card-v2">
                                    <div class="kt-user-card-v2__details">
                                        <span class="kt-user-card-v2__name">` + nom + `</span><br>
                                        <span class="kt-user-card-v2__desc">` + adresse + `, ` + code + `, ` + ville + `</span>
                                    </div>
                                </div>
                            </span>`);
                        }
                        else {
                            return "Non renseigné";
                        }
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var nom = row.fields.pj_nom;
                        var doc = row.fields.pj_document;
                        var res = ''
                        for (var i=0; i<nom.length; i++) {
                            res += `
                            <span>
                                <div class="kt-user-card-v2">
                                    <div class="kt-user-card-v2__details">
                                        <span class="kt-user-card-v2__name">` + nom[i] + `</a><br>
                                        <a href="` + doc[i] + `" class="kt-user-card-v2__desc">Voir</a>
                                    </div>
                                </div>
                            </span>`
                        }
                        return res;
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var id = row.pk;
                        var statut = row.fields.statut;
                        if (statut == 'En attente')
                        {
                            return (`<span class="kt-badge kt-badge--warning kt-badge--inline" id="active_`+id+`">En attente</span>`);
                        }
                        else if (statut == 'En cours')
                        {
                            return (`<span class="kt-badge kt-badge--info kt-badge--inline" id="active_`+id+`">En cours</span>`);
                        }
                        else if (statut == 'Historique')
                        {
                            return (`<span class="kt-badge kt-badge--dark kt-badge--inline" id="active_`+id+`">Historique</span>`);
                        }
                    }
                }
            ]
        }
    );

});