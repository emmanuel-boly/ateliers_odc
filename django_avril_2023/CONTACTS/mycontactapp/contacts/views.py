from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
import vobject
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from vobject.base import ParseError


def import_contacts(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        vcf_file = request.FILES.get('vcf_file')
        if vcf_file:
            imported_contacts = 0
            failed_contacts = 0
            
            for vcard in vobject.readComponents(vcf_file.read().decode()):
                try:
                    contact = Contact(owner=request.user)
                    contact.name = vcard.n.value.given + ' ' + vcard.n.value.family
                    contact.email = vcard.email.value if hasattr(vcard, 'email') else ''
                    contact.phone = vcard.tel.value if hasattr(vcard, 'tel') else ''
                    contact.birthday = vcard.bday.value if hasattr(vcard, 'bday') else None
                    contact.save()
                    print(imported_contacts)
                    imported_contacts += 1
                except ParseError:
                    failed_contacts += 1
                    continue

            if failed_contacts:
                messages.warning(request, f"{failed_contacts} contacts n'ont pas pu être importés.")
            messages.success(request, f"{imported_contacts} contacts importés.")
        else:
            messages.error(request, "Veuillez sélectionner un fichier VCF à importer.")
        return redirect('contacts_list')
    return render(request, 'contacts/import_contacts.html')


"""
def import_contacts(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        vcf_file = request.FILES.get('vcf_file')
        if vcf_file:
            imported_contacts = 0
            for vcard in vobject.readComponents(vcf_file.read().decode()):
                contact = Contact(owner=request.user)
                contact.name = vcard.n.value.given + ' ' + vcard.n.value.family
                contact.email = vcard.email.value if hasattr(vcard, 'email') else ''
                contact.phone = vcard.tel.value if hasattr(vcard, 'tel') else ''
                contact.birthday = vcard.bday.value if hasattr(vcard, 'bday') else None
                contact.save()
                imported_contacts += 1
            messages.success(request, f"{imported_contacts} contacts importés.")
        else:
            messages.error(request, "Veuillez sélectionner un fichier VCF à importer.")
        return redirect('contacts_list')
    return render(request, 'contacts/import_contacts.html')
"""
def export_contacts(request):
    if not request.user.is_authenticated:
        return redirect('login')

    contacts = Contact.objects.filter(owner=request.user)
    vcards = []
    for contact in contacts:
        vcard = vobject.vCard()
        name = vobject.vcard.Name(given=contact.name.split(' ')[0], family=' '.join(contact.name.split(' ')[1:]))
        vcard.add('n').value = name
        vcard.add('fn').value = contact.name
        if contact.email:
            vcard.add('email').value = contact.email
        if contact.phone:
            vcard.add('tel').value = contact.phone
        if contact.birthday:
            vcard.add('bday').value = contact.birthday.isoformat()
        vcards.append(vcard.serialize())

    response = HttpResponse('\n'.join(vcards), content_type='text/vcard')
    response['Content-Disposition'] = 'attachment; filename=contacts.vcf'
    return response

def contacts_list(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(owner=request.user)
        return render(request, 'contacts/contacts_list.html', {'contacts': contacts})
    else:
        return redirect('login')

def create_contact(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contacts_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/create_contact.html', {'form': form})


def update_contact(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/update_contact.html', {'form': form})


def delete_contact(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    contact.delete()
    return redirect('contacts_list')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('contacts_list')
    else:
        form = UserCreationForm()
    return render(request, 'contacts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('contacts_list')
    else:
        form = AuthenticationForm()
    return render(request, 'contacts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
