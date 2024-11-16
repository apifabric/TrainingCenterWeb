import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CertificateHomeComponent } from './home/Certificate-home.component';
import { CertificateNewComponent } from './new/Certificate-new.component';
import { CertificateDetailComponent } from './detail/Certificate-detail.component';

const routes: Routes = [
  {path: '', component: CertificateHomeComponent},
  { path: 'new', component: CertificateNewComponent },
  { path: ':id', component: CertificateDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Certificate-detail-permissions'
      }
    }
  }
];

export const CERTIFICATE_MODULE_DECLARATIONS = [
    CertificateHomeComponent,
    CertificateNewComponent,
    CertificateDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CertificateRoutingModule { }