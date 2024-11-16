import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {COURSEMATERIAL_MODULE_DECLARATIONS, CourseMaterialRoutingModule} from  './CourseMaterial-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CourseMaterialRoutingModule
  ],
  declarations: COURSEMATERIAL_MODULE_DECLARATIONS,
  exports: COURSEMATERIAL_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CourseMaterialModule { }