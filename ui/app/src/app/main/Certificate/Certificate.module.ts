import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CERTIFICATE_MODULE_DECLARATIONS, CertificateRoutingModule} from  './Certificate-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CertificateRoutingModule
  ],
  declarations: CERTIFICATE_MODULE_DECLARATIONS,
  exports: CERTIFICATE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CertificateModule { }