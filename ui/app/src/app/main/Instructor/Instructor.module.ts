import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {INSTRUCTOR_MODULE_DECLARATIONS, InstructorRoutingModule} from  './Instructor-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    InstructorRoutingModule
  ],
  declarations: INSTRUCTOR_MODULE_DECLARATIONS,
  exports: INSTRUCTOR_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class InstructorModule { }