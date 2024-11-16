import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {INSTRUCTORASSIGNMENT_MODULE_DECLARATIONS, InstructorAssignmentRoutingModule} from  './InstructorAssignment-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    InstructorAssignmentRoutingModule
  ],
  declarations: INSTRUCTORASSIGNMENT_MODULE_DECLARATIONS,
  exports: INSTRUCTORASSIGNMENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class InstructorAssignmentModule { }