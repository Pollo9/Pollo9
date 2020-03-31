"use strict";
var KTDatatablesSearchOptionsAdvancedSearch=function() {
    $.fn.dataTable.Api.register("column().title()", function() {
        return $(this.header()).text().trim()
    }
    );
    return {
        init:function() {
            var t;
            t=$("#kt_table").DataTable( {
                responsive:!0, dom:"<'row'<'col-sm-12'tr>>\t\t\t<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7 dataTables_pager'lp>>", lengthMenu:[5, 10, 25, 50], pageLength:10, language: {
                    lengthMenu: "Display _MENU_"
                }
                , searchDelay:500, processing:!0, serverSide:!0, ajax: {
                    url:"/dossiers", type:"POST", data: {
                        columnsDef: ["ID", "Nom<br>Prénom", "Téléphone<br>Email", "Date de création<br>Dernière modification", "Créateur dossier", "Installateur<br>Commercial", "Status", "Actions"]
                    }
                }
                , columns:[ {
                    data: "ID"
                }
                , {
                    data: "Nom<br>Prénom"
                }
                , {
                    data: "Téléphone<br>Email"
                }
                , {
                    data: "Date de création<br>Dernière modification"
                }
                , {
                    data: "Créateur dossier"
                }
                , {
                    data: "Installateur<br>Commercial"
                }
                , {
                    data: "Status"
                }
                , {
                    data: "Actions"
                }]
                , initComplete:function() {
                    this.api().columns().every(function() {
                        switch(this.title()) {
                            case"Status":
                                var t= {
                                1: {
                                    title: "Dossier incomplet", class: "kt-badge--warning"
                                }
                                , 2: {
                                    title: "Dossier complet", class: " kt-badge--brand"
                                }
                                , 3: {
                                    title: "Etude banque", class: " kt-badge--primary"
                                }
                                , 4: {
                                    title: "Financement accordé", class: " kt-badge--success"
                                }
                                , 5: {
                                    title: "Financement refusé", class: " kt-badge--danger"
                                }
                                , 6: {
                                    title: "Terminer", class: " kt-badge--info"
                                }
                                }
                                ;
                                this.data().unique().sort().each(function(a, e) {
                                    $('.kt-input[data-col-index="6"]').append('<option value="'+a+'">'+t[a].title+"</option>")
                                }
                                );
                                break;
                        }
                    }
                    )
                }
                ,columnDefs:[ {
                    targets:-1, title:"Actions", orderable:!1, render:function(t, a, e, n) {
                        return'                        <span class="dropdown">                            <a href="#" class="btn btn-sm btn-clean btn-icon btn-icon-md" data-toggle="dropdown" aria-expanded="true">                              <i class="la la-ellipsis-h"></i>                            </a>                            <div class="dropdown-menu dropdown-menu-right">                                <a class="dropdown-item" href="#"><i class="la la-edit"></i> Edit Details</a>                                <a class="dropdown-item" href="#"><i class="la la-leaf"></i> Update Status</a>                                <a class="dropdown-item" href="#"><i class="la la-print"></i> Generate Report</a>                            </div>                        </span>                        <a href="#" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="View">                          <i class="la la-edit"></i>                        </a>'
                    }
                }
                , {
                    targets:7, render:function(t, a, e, n) {
                        var i= {
                            1: {
                                title: "Dossier incomplet", class: "kt-badge--warning"
                            }
                            , 2: {
                                title: "Dossier complet", class: " kt-badge--brand"
                            }
                            , 3: {
                                title: "Etude banque", class: " kt-badge--primary"
                            }
                            , 4: {
                                title: "Financement accordé", class: " kt-badge--success"
                            }
                            , 5: {
                                title: "Financement refusé", class: " kt-badge--danger"
                            }
                            , 6: {
                                title: "Terminer", class: " kt-badge--info"
                            }
                        };
                        return void 0===i[t]?t:'<span class="kt-badge '+i[t].class+' kt-badge--inline kt-badge--pill">'+i[t].title+"</span>"
                    }
                }
                ]
            }
            ),
            $("#kt_search").on("click", function(a) {
                a.preventDefault();
                var e= {}
                ;
                $(".kt-input").each(function() {
                    var t=$(this).data("col-index");
                    e[t]?e[t]+="|"+$(this).val(): e[t]=$(this).val()
                }
                ), $.each(e, function(a, e) {
                    t.column(a).search(e||"", !1, !1)
                }
                ), t.table().draw()
            }
            ),
            $("#kt_reset").on("click", function(a) {
                a.preventDefault(), $(".kt-input").each(function() {
                    $(this).val(""), t.column($(this).data("col-index")).search("", !1, !1)
                }
                ), t.table().draw()
            }
            ),
            $("#kt_datepicker").datepicker( {
                todayHighlight:!0, templates: {
                    leftArrow: '<i class="la la-angle-left"></i>', rightArrow: '<i class="la la-angle-right"></i>'
                }
            }
            )
        }
    }
}

();
jQuery(document).ready(function() {
    KTDatatablesSearchOptionsAdvancedSearch.init()
}

);

