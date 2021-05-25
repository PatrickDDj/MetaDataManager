from django.shortcuts import render, redirect
from django.urls import reverse

from . import utils

def home(request):
    tables = utils.get_all_tables()
    context = {'tables':tables}
    return render(request, 'home.html', context)


def create_table(request):
    table_name = request.POST['table_name']
    columns = request.POST['columns'].split(',')
    utils.create_table(table_name, columns)
    return redirect('home')


def to_create_table(request):
    return render(request, 'table_create.html')


def show_records(request, table_name):
    # table_name = request.GET['table_name']
    columns, records_index = utils.show_table(table_name)
    context = {
        'table_name': table_name,
        'columns': columns,
        # 'records': records,
        # 'index': index
        'records_index': records_index
    }
    return render(request, 'show_records.html', context)


def add_record(request, table_name):
    record = request.POST.getlist('record')
    utils.add_record(table_name, record)
    return redirect('show_records', table_name=table_name)


def delete_record(request, table_name, index):
    utils.delete_record(table_name, index)
    return redirect('show_records', table_name=table_name)


def edit_record(request, table_name, index):
    if request.method == "GET":
        columns, record = utils.get_record(table_name, index)
        context = {
            'table_name': table_name,
            'index': index,
            'columns': columns,
            'record': record
        }
        return render(request, 'edit_record.html', context)
    else:
        record = request.POST.getlist('record')
        utils.edit_record(table_name, index, record)
        return redirect('show_records', table_name=table_name)

def delete_table(request, table_name):
    utils.delete_table(table_name)
    return redirect('home')

