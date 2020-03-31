$(document).ready(function() 
{
    //Create the table
    var table = $('#kt_table').DataTable
    ( 
        {
            "ajax": 
            {
                "url": "/ajax_missions",
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
                        var id = row.pk;
                        return (`
                            <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid" for="` + id + `">
                                <input type="checkbox" value="` + id + `" id="` + id + `" name="mission_selectionnee" class="kt-checkable">
                                <span></span>
                            </label>`);
                    },
                    "orderable": false,
                    "width": "1%",
                },
                {
                    "render": function ( data, type, row )
                    {
                        var jour = row.fields.jour;
                        var res = '';
                        if (jour != "None")
                        {
                            var options = {year: 'numeric', month: 'long', day: 'numeric'};
                            var jour = new Date(jour)
                            res += jour.toLocaleDateString('fr-FR',options);
                        }
                        return res; 
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var debut = row.fields.debut;
                        var fin = row.fields.fin;
                        var res = '';
                        if (debut != "None" & fin != "None")
                        {
                            res += debut;
                            res += '<br>';
                            res += fin;
                        }
                        return res; 
                    }
                },
                {
                    "render": function ( data, type, row )
                    {   
                        var id = row.fields.consultant_id;
                        var avatar = row.fields.consultant_avatar;
                        var prenom = row.fields.consultant_prenom;
                        var nom = row.fields.consultant_nom;
                        var group = row.fields.consultant_groups;
                        var url_profil = "/administrateur/profil_consultant/" + id;
                        if (id) {
                            return (`
                            <span>
                                <div class="kt-user-card-v2">
                                    <div class="kt-user-card-v2__pic">
                                        <img src="` + avatar + `" alt="photo">
                                    </div>
                                    <div class="kt-user-card-v2__details">
                                        <a href="` + url_profil + `" class="kt-user-card-v2__name">` + prenom + ` ` + nom + `</a>
                                        <span class="kt-user-card-v2__desc">` + group + `</span>
                                    </div>
                                </div>
                            </span>`);
                        }
                        else {
                            return 'Non renseigné';
                        }                        
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var id = row.fields.client_id;
                        var nom = row.fields.client_nom;
                        var avatar = row.fields.client_avatar;
                        var url_profil = "/administrateur/profil_client/" + id;
                        if (id) {
                            return (`
                            <span>
                                <div class="kt-user-card-v2">
                                    <div class="kt-user-card-v2__pic">
                                        <img src="` + avatar + `" alt="photo">
                                    </div>
                                    <div class="kt-user-card-v2__details">
                                        <a href="` + url_profil + `" class="kt-user-card-v2__name">` + nom + `</a>
                                    </div>
                                </div>
                            </span>`);
                        }
                        else {
                            return ('Non renseigné');
                        }
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var id = row.pk;
                        var statut = row.fields.statut;
                        return (`<span class="kt-badge kt-badge--info kt-badge--inline" id="active_`+id+`">`+ statut +`</span>`);
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var type = row.fields.type;
                        return type;
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var csrf = "{% csrf_token %}"
                        var id = row.pk;
                        var url_profil = "/administrateur/profil_mission/" + id;
                        return (`
                            <a id="button" href="` + url_profil + `" class="btn btn-sm btn-clean btn-icon btn-icon-md" style="padding: 0.06rem .25rem;" title="Profil du consultant">
                                <i class="icon-eye"></i>
                            </a>
                            <a class="btn btn-sm btn-clean btn-icon btn-icon-md" style="padding: 0.06rem .25rem;" onclick="openModalDelete(` + id + `)" id="supprimer_mission_` + id + `" alt="Supprimer" title="Supprimer la mission" data-id=` + id + `>
                                <i class="icon-trash"></i>
                            </a>`);
                    }

                }
            ]
        }
    );

    // Check/uncheck all checkboxes in the table
    $('#select_all1').on('click', function()
    {
        var rows = table.rows({ 'search': 'applied' }).nodes();
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
        if (document.getElementById('select_all2').checked == true)
        {
            document.getElementById('select_all2').checked = false;
        }
        else
        {
            document.getElementById('select_all2').checked = true;
        }
    });

    // Check/uncheck all checkboxes in the table
    $('#select_all2').on('click', function()
    {
        var rows = table.rows({ 'search': 'applied' }).nodes();
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
        if (document.getElementById('select_all1').checked == true)
        {
            document.getElementById('select_all1').checked = false;
        }
        else
        {
            document.getElementById('select_all1').checked = true;
        }
    });

    // When a checkboxe is cheked display menu
    $('#kt_table').on('click',"input[type='checkbox']", function()
    {
        var nombre_row_checked = $('input[name="mission_selectionnee"]:checked').length;
        var total_rows = table.rows().count()
        if (nombre_row_checked > 0)
        {
            document.getElementById("nombre_de_mission").innerHTML = nombre_row_checked + " sélectionnées";
            document.getElementById('menu_to_display').style.display = 'flex';
        }
        else
        {
            document.getElementById("nombre_de_mission").innerHTML = total_rows + " total";
            document.getElementById('menu_to_display').style.display = 'none';
        }
        var row = $(this).closest('tr');
        if(this.checked)
        {
            row.addClass('selected');
        } 
        else 
        {
            row.removeClass('selected');
        }     
    });
});