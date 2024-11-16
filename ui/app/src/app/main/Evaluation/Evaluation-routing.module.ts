import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EvaluationHomeComponent } from './home/Evaluation-home.component';
import { EvaluationNewComponent } from './new/Evaluation-new.component';
import { EvaluationDetailComponent } from './detail/Evaluation-detail.component';

const routes: Routes = [
  {path: '', component: EvaluationHomeComponent},
  { path: 'new', component: EvaluationNewComponent },
  { path: ':id', component: EvaluationDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Evaluation-detail-permissions'
      }
    }
  }
];

export const EVALUATION_MODULE_DECLARATIONS = [
    EvaluationHomeComponent,
    EvaluationNewComponent,
    EvaluationDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EvaluationRoutingModule { }