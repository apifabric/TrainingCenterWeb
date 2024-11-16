import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {ENROLLMENT_MODULE_DECLARATIONS, EnrollmentRoutingModule} from  './Enrollment-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    EnrollmentRoutingModule
  ],
  declarations: ENROLLMENT_MODULE_DECLARATIONS,
  exports: ENROLLMENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class EnrollmentModule { }