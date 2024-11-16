import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {STUDENT_MODULE_DECLARATIONS, StudentRoutingModule} from  './Student-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    StudentRoutingModule
  ],
  declarations: STUDENT_MODULE_DECLARATIONS,
  exports: STUDENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class StudentModule { }